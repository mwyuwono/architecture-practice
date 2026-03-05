Role: You are acting as my Lead Architectural Coordinator and Technical Clerk for a new residential design project.

Objective: Help me manage project documentation, technical specifications, and building code compliance while I handle the primary design in AutoCAD.

Task 1: Environment Setup
Please create the following directory structure in this folder:

/Drawings (for .dwg files and exports)

/Data_Raw (for CSV/JSON data extractions from AutoCAD)

/Schedules (for agent-generated Markdown tables)

/Specs (for material and assembly details)

/Code_Research (for local zoning and building code notes)

Task 2: Create agent.md (The Project Brain)
Initialize an agent.md file at the root. This file must track the "Global State" of the project. Include the following placeholder sections:

Project Overview: (Site address, Climate Zone, Occupancy Type)

Design Logic & Constraints: (e.g., "All exterior walls must be 6-inch nominal," "Minimum hallway width 36 inches")

Data Source Mapping: (Explain that .csv files in /Data_Raw are the source of truth for all schedules)

Change Log: (A chronological list of design decisions)

Task 3: Establish the Workflow Protocol
Define a "Verification Protocol" in agent.md. Whenever I provide new data or design updates:

Parse the input for dimensions, materials, or counts.

Cross-reference the data against the established project constraints and known building codes.

Update the relevant .md files in /Schedules or /Specs.

Alert me if a design choice (like a window size or door swing) seems to conflict with a previous instruction or a code requirement.

Confirmation:
Once the folder structure and agent.md are created, please ask me for the initial Project Identity details (Location, Square Footage goals, and Architectural Style) to begin our first "State" entry.