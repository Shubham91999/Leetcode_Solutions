class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        execution_times = [0] * n  # List to maintain execution of tasks 

        call_stack = [] # Stack to store functions in sequence
        prev_start_time = 0

        for log in logs:
            func_id, call_type, timestamp = log.split(":")
            func_id = int(func_id) # Converting from str to int
            timestamp = int(timestamp)

            if call_type == "start": # If function is starting 
                if call_stack:  # If any function already present in stack
                    # New function came in, current running function will stop, so adding executed time (timestamp-prev_start_time)
                    execution_times[call_stack[-1]] += timestamp - prev_start_time 
                # If nothing in call_stack, append function and set current timestamp as its start time
                call_stack.append(func_id)
                prev_start_time = timestamp

            else:  # Call type is end
                execution_times[call_stack.pop()] += timestamp - prev_start_time + 1
                prev_start_time = timestamp + 1

        return execution_times



