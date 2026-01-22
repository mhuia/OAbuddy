## Running Long-Term Jobs on a Server Using `screen`, `tmux`, or `nohup` 

When you need to run Python scripts on a server for an extended period—such as downloading **ERA5** or **CMEMS** datasets—you can use the `screen`, `tmux`, or `nohup` commands.
This allows tasks to continue running even if the network connection to the server is interrupted.

-------------------------------------------------------------------------------------------------

### Commonly Used `screen` Commands (interactive debugging)

- **Create a new screen session**
  ***`Bash`***
  ```bash
  
    # Create a new screen session
    screen -S <session_name>
    conda activate <your_envirnment_name>
    python your_python_script.py

    # Detach from the current screen session (the task keeps running)
    # Press the following key sequence:
    Ctrl + A, then press D

    # List all existing screen sessions
    screen -ls

    # Reattach to a specific screen session
    screen -r <session_id_or_name>

    # Terminate a screen session
    screen -X -S <session_id_or_name> quit
    # (Alternatively, you can reattach to the session and type `exit` to close it)

### Commonly Used `tmux` Commands (interactive debugging)

Here is the [man page](https://man7.org/linux/man-pages/man1/tmux.1.html) and the [wiki](https://github.com/tmux/tmux/wiki) of `tmux`. You can get more details about `tmux`.

- **Create a new tmux session**
  ***`Bash`***
  ```bash
  
    # Create a new tmux session
    tmux new -s <session_name>
    # After creating a new tmux session,
    # you are in the new tmux seesion automatically.
    # Inside your new tmux session,
    # run commands you need, like:
    conda activate <your_envirnment_name>
    python your_python_script.py

    # Detach from the current tmux session (the task keeps running)
    # Press the following key sequence:
    <Ctrl + B>, <D>

    # List all existing tmux sessions
    tmux ls

    # Reattach to a specific tmux session
    tmux attach -t <session_id_or_name>

    # Terminate a tmux session
    tmux kill-session -t <session_id_or_name>

    # Alternatively, you can terminate a tmux session
    # inside it using:
    exit
    # or
    <Ctrl + D>
    
-------------------------------------------------------------------------------------------------

### A More Professional `bash + nohup + log` Workflow (production runs)

For long-running Python jobs (e.g., downloading ERA5 or CMEMS data, model training, or large-scale batch processing), a **bash + nohup + explicit logging** workflow is more professional, reproducible, and suitable for production or HPC environments.

- **1. Create a Dedicated Bash Script `run_job.sh`**
    ```bash
    #!/bin/bash

    # Environment setup
    source ~/.bashrc
    conda activate <your_environment_name>

    # Working directory
    cd /path/to/your/project || exit 1

    # Run Python script
    python your_python_script.py

- **2. Make the script executable and Launch the Job Using `nohup` with Log Redirection**
  ***`Bash`***
    ```bash
    # Make the script executable
    chmod +x run_job.sh 

    nohup ./run_job.sh > job_$(date +%Y%m%d_%H%M%S).log 2>&1 &
    # 'nohup' keeps the job running after SSH disconnects
    # '>' edirects standard output (stdout) to a log file
    # '2>&1' edirects standard error (stderr) to the same log file
    # '&' runs the job in the background
    # Timestamped log filenames prevent overwriting and improve traceability

- **3. Check Running Processes & Monitor Logs in Real Time**
  ***`Bash`***
    ```bash
    ps -u $USER | grep your_python_script.py
    tail -f logs/job_YYYYMMDD_HHMMSS.log

- **4. Stop a Running Job**
  ***`Bash`***
    ```bash
    ps -ef | grep your_python_script.py
    kill <PID>
