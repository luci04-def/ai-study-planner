def generate_schedule(subjects, weekday_hours, weekend_hours):
    # Calculate priority score
    for s in subjects:
        s["priority"] = s["credits"] * (6 - s["confidence"])

    total_priority = sum(s["priority"] for s in subjects)

    # Total weekly hours
    total_hours = weekday_hours * 5 + weekend_hours * 2

    # Allocate hours
    for s in subjects:
        s["allocated"] = round(
            (s["priority"] / total_priority) * total_hours, 1
        )

    # Create simple weekly plan
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    schedule = {}

    for day in days:
        hours = weekday_hours if day in days[:5] else weekend_hours
        schedule[day] = []

        sorted_subs = sorted(subjects, key=lambda x: -x["priority"])
        i = 0

        while hours > 0:
            sub = sorted_subs[i % len(sorted_subs)]
            schedule[day].append(sub["name"])
            hours -= 1
            i += 1

    return subjects, schedule
