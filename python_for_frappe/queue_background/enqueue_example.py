import frappe

def background_job_example(docname):
    print(f"Processing doc: {docname}")

# Enqueue a job
frappe.enqueue('queue_background.enqueue_example.background_job_example',
               docname='TODO-ID', queue='default', timeout=300)
