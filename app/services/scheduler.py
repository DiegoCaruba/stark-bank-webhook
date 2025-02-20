import time
import threading
import schedule


def run_jobs(interval=1) -> threading.Event:
    """Runs scheduled jobs in a separate thread"""
    stop_event = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not stop_event.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()

    return stop_event
