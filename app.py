import streamlit as st
from scheduler import generate_schedule

st.set_page_config(page_title="AI Study Planner", layout="centered")

st.title("📚 AI Study Planner for Engineering Students")

st.write("Generate a smart personalized study schedule.")

num_subjects = st.number_input(
    "Number of subjects", min_value=1, max_value=6, value=3
)

subjects = []

st.subheader("Enter Subject Details")

for i in range(num_subjects):
    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input(f"Subject {i+1}", f"Subject {i+1}")

    with col2:
        credits = st.number_input(
            f"Credits {i+1}", min_value=1, max_value=5, value=3
        )

    with col3:
        confidence = st.slider(
            f"Confidence {i+1}", 1, 5, 3
        )

    subjects.append({
        "name": name,
        "credits": credits,
        "confidence": confidence
    })

st.subheader("Study Time Availability")

weekday_hours = st.number_input(
    "Weekday hours per day", min_value=1, max_value=12, value=3
)

weekend_hours = st.number_input(
    "Weekend hours per day", min_value=1, max_value=12, value=5
)

if st.button("Generate Study Plan 🚀"):

    updated_subjects, schedule = generate_schedule(
        subjects, weekday_hours, weekend_hours
    )

    st.subheader("📊 Weekly Subject Allocation")

    for s in updated_subjects:
        st.write(
            f"**{s['name']}** → {s['allocated']} hours/week"
        )

    st.subheader("🗓 Weekly Schedule")

    for day, tasks in schedule.items():
        st.write(f"**{day}:** {', '.join(tasks)}")

    st.success(
        "More time allocated to low-confidence subjects automatically."
    )

    st.info(
        "High-priority topics are scheduled earlier to improve retention."
    )
