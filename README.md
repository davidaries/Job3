# Job3
Job 3.txt

Goals:
1. Starting down the UI Widgetizing path
2. Reading and writing pdata

Widgeting Goal: UIs with "no-programming" - the programmer is not directly developing screens the user sees, rather providing to the SME a library and tools to work with so the SME can create the UIs. 

The developer creates awesome (but limited) set of templates and widgets
  - templates are each a standard layout (typically with a few widgets in it)
  - widgets (the functionality pieces) that are placed within templates

The SME, in the UI development tool, specifies the UI by choosing the:
  - the template
  - any additional widgets (if such can and need to be added to the template)
  - the specifications for the widgets (what to display in the widget)
  - all of which gets specified in a table

For now, though, we are just going to add widgets. 


========================================================================================
What build:

For now, we aren't going to use the timer functions. We will again in the future, so we can leave them as is in the code (Or not, as when we do, the timing will be specific to providers and the task they are doing). 

All four staffers show up at the start. 

Staffers have four different roles: Receptionist, Assistant, Provider, Lab Technician.

To start, all four staffers their Home Screen visible.

When they select one of the persons, it takes them to their Task Screen.

On the task screen they enter or modify any data as needed, then hit the submit button. 

This does five things:
- for each data element appends a row to pdata  (especially protocol, step, k, vt, v)*
- also writes that each appended row to the visible log
- returns the staffer to their Home Screen

* for datm - do a global increment
  for meta_datm set to 1
  for person, encounter - use the person and encounter (of that person)
  for event_dts - use datetime.datetime.now().timestamp()
