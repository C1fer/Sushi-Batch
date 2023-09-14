import console_utils as cu
from job_queue import JobQueue


main_queue = JobQueue()


# Handle main queue options
def main_queue_options(task):
    while True:
        # Show menu and options
        options = {
            "1": "Start queue",
            "2": "Run selected jobs",
            "3": "Remove selected jobs",
            "4": "Clear queue",
            "5": "Clear completed and failed jobs",
            "6": "Return to main menu",
        }
        main_queue.show(task)
        cu.show_menu_options(options)

        # Get selected option
        choice = cu.get_choice(1, 6)

        # Handle user-selected options
        if cu.confirm_action():
            match choice:
                case 1:
                    main_queue.run_jobs("all")
                case 2:
                    selected_jobs = main_queue.select_jobs(
                        "Select jobs to run (e.g: 1, 5-10): "
                    )
                    if selected_jobs is not None and cu.confirm_action():
                        main_queue.run_jobs(selected_jobs)
                case 3:
                    selected_jobs = main_queue.select_jobs(
                        "Select jobs to remove from queue (e.g: 1, 5-10): "
                    )
                    if selected_jobs is not None and cu.confirm_action():
                        main_queue.remove_jobs(selected_jobs)
                        cu.print_success(f"{len(selected_jobs)} job(s) removed from queue.")
                        if not main_queue.contents:
                            break
                case 4:
                    main_queue.clear()
                    cu.print_success("Queue cleared.")
                    break
                case 5:
                    main_queue.clear_completed_jobs()
                    # Return to main menu if queue was cleared
                    if not main_queue.contents:
                        break
                case 6:
                    break


# Handle temp queue options
def temp_queue_options(temp_queue, task):
    while True:
        # Show menu and options
        options = {
            "1": "Run all jobs",
            "2": "Run selected jobs",
            "3": "Add all jobs to queue",
            "4": "Add selected jobs to queue",
            "5": "Return to main menu",
        }
        temp_queue.show(task)
        cu.show_menu_options(options)

        # Get selected option
        choice = cu.get_choice(1, 5)

        # Handle user-selected options
        if cu.confirm_action():
            match choice:
                case 1:
                    # Add all jobs to main queue before executing them
                    main_queue.add_jobs("all", temp_queue.contents, task)
                    temp_queue.run_jobs("all")
                    break
                case 2:
                    selected_jobs = temp_queue.select_jobs(
                        "Select jobs to run (e.g: 1, 5-10): "
                    )
                    if selected_jobs is not None and cu.confirm_action():
                        # Add selected jobs to main queue before executing them
                        main_queue.add_jobs(selected_jobs, temp_queue.contents, task)
                        temp_queue.run_jobs(selected_jobs)
                        break
                case 3:
                    # Add all jobs to main queue
                    main_queue.add_jobs("all", temp_queue.contents, task)
                    cu.print_success(f"{len(temp_queue.contents)} job(s) added to queue.")
                    break
                case 4:
                    selected_jobs = details_queue.select_jobs(
                        "Select jobs to add to the queue (e.g: all, 1, 5-10): "
                    )
                    if selected_jobs is not None and cu.confirm_action():
                        # Add selected jobs to main queue
                        main_queue.add_jobs(selected_jobs, temp_queue.contents, task)
                        cu.print_success(f"{len(selected_jobs)} job(s) added to queue.")
                        break
                case 5:
                    break
