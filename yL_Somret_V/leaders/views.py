from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Race, Riddle, Leader
from django.utils import timezone
from .models import Race, Zone, Riddle


#@login_required add when authenticication is required
def leadersHome(request):
    return render(request, '../templates/leaderHome.html')



def make_questions(request):
    if request.method == "POST":
        race_name = request.POST.get("race_name")
        race = Race.objects.create(name=race_name)

        # Create the Race entry
        race = Race.objects.create(name=race_name)

        # Loop through zones
        zones_data = []
        zone_index = 1
        while f"zone-{zone_index}-questions[]" in request.POST:
            questions = request.POST.getlist(f"zone-{zone_index}-questions[]")
            answers = request.POST.getlist(f"zone-{zone_index}-answers[]")

            if questions and answers:
                zone = Zone.objects.create(race=race, number=zone_index)
                riddles = []

                # Save each riddle in this zone
                for q, a in zip(questions, answers):
                    riddle = Riddle.objects.create(zone=zone, question=q, answer=a)
                    riddles.append({'question': q, 'answer': a})

                zones_data.append({
                    'zone_number': zone.number,
                    'riddles': riddles
                })

            zone_index += 1  # Move to the next zone

        # Redirect to savedQuestions.html with race and zone data
        return render(request, "savedQuestions.html", {"race": race, "zones": zones_data})

    return render(request, "makeQuestions.html")

def saved_races(request):
    # Get all races
    races = Race.objects.all()

    # Prepare data to display
    saved_races_data = []
    for race in races:
        zones_data = []
        for zone in race.zones.all():  # Get all zones related to the race
            riddles = [{'question': riddle.question, 'answer': riddle.answer} for riddle in zone.riddles.all()]
            zones_data.append({'zone_number': zone.number, 'riddles': riddles})

        saved_races_data.append({
            'race_name': race.name,
            'zones': zones_data
        })

    return render(request, "savedQuestions.html", {"saved_races": saved_races_data})

# Edit Race
def edit_race(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    # Logic for editing the race (can be a form to modify the race)
    return render(request, "editRace.html", {'race': race})

# Launch Race
def launch_race(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    # Logic to launch the race (e.g., setting status or creating a new event)
    return render(request, "launchRace.html", {'race': race})

def delete_race(request, race_id):

    race = get_object_or_404(Race, id=race_id)
    race.delete()  # Delete the race
    return redirect('saved_races')  # Redirect back to the saved races page



