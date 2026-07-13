from db import save_job, get_jobs
save_job(
    "Prompt Engineer",
    "OpenAI",
    "Remote",
    "https://openai.com"
)

print(get_jobs())