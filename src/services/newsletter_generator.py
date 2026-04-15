from jinja2 import Environment, FileSystemLoader
from services.llm_service import llm_service
from tools.mcp_tools import get_campus_events, get_course_reminders, get_weather_forecast

env = Environment(loader=FileSystemLoader('/app/templates'))

def generate_personalized_newsletter(user):
    events = get_campus_events()
    courses = get_course_reminders(user.program)
    weather = get_weather_forecast(f"{user.college},IN")

    e_summary = llm_service.generate_text(f"Summarize these events: {events}")
    c_summary = llm_service.generate_text(f"Summarize these course reminders: {courses}")
    w_summary = llm_service.generate_text(f"Summarize this weather: {weather}")

    template = env.get_template('newsletter_main.j2')
    return template.render(
        events_summary=e_summary,
        courses_summary=c_summary,
        weather_summary=w_summary
    )
