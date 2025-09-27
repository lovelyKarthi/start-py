# Scheduler example in hooks.py
scheduler_events = {
    'daily': [
        'my_app.tasks.daily_task'
    ],
    'hourly': [
        'my_app.tasks.hourly_task'
    ]
}

def daily_task():
    print('Daily task executed')
