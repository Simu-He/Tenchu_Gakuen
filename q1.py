import logging
from datetime import datetime
from functools import wraps
import os

log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)
action_list_MAX = 9223372036854775808


logging.basicConfig(
    filename=os.path.join(log_directory, "action_log.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def log_and_execute(human_id, time, location, action_id, *action_params):
    

    @wraps(action_id)
    def wrapped_action(*args, **kwargs):
        try:
            action_function = action_list[action_id]
            logging.info(
                f"Action executed: {action_function.__name__} | "
                f"Human ID: {human_id}, Time: {time}, Location: {location}"
            )

            return action_function(human_id, time, location, *action_params)
        except Exception as e:
            logging.error(f"Error during action execution: {e}")
            raise

    wrapped_action()



if __name__ == "__main__":
    human_id = "4"
    x = 3
    time = datetime(2024,4,x,16,44,44)
    assert x > 0 and x < 15
    location = "ijigen shokoko"


    log_and_execute(human_id, time, location, 9223372036854775809,"unkonw_rule")
