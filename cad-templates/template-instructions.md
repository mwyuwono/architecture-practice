You are helping prepare an AutoCAD for Mac template for residential architectural drafting. Your objective is to automate as much of the template setup as possible, produce all files and scripts you can, and clearly separate what can be automated from what requires manual setup inside AutoCAD for Mac.

Context and goals:
- Platform: AutoCAD for Mac
- Purpose: a reusable office template for residential architectural drawings
- Standards target: U.S. National CAD Standard / Uniform Drawing System best practices
- Units: imperial
- Output target: a template-ready drawing package and supporting setup files/instructions
- Priority: automate as much as realistically possible, then provide a precise manual checklist for anything AutoCAD for Mac does not expose well to scripting or file-based setup

Important constraints:
- Do not assume Windows-only features, dialogs, file paths, APIs, or workflows.
- Be explicit whenever something is AutoCAD-for-Mac-specific.
- If a feature is uncertain or not reliably automatable on AutoCAD for Mac, do not pretend it is. Flag it as manual.
- Prefer robust, minimal, standards-oriented setup over overengineering.
- Keep the result clean and maintainable for future office use.

What I need you to produce:
1. A complete automation package to initialize a new template drawing as far as possible.
2. A clear inventory of deliverables.
3. A step-by-step manual follow-up list for anything not handled automatically.
4. Notes on assumptions, limitations, and risks.
5. Suggested future enhancements if fuller automation becomes possible.

Primary deliverables to create:
- A master instruction file explaining the setup
- Any AutoCAD-compatible script files you can generate, such as .scr
- Any AutoLISP files that are likely usable in AutoCAD for Mac, if appropriate
- A human-readable layer standard file, such as CSV or TXT, that lists layers and properties
- A template specification document that describes the intended final DWT configuration
- A manual checklist for title block, page setup, text styles, dimension styles, plot styles, annotation scales, and layouts
- A validation checklist to verify the final template after setup

Mission:
Create an “NCS Residential Template Setup Package” that prepares a template drawing with the following best-practice configuration.

Required drawing configuration:
A. Units and base drawing setup
- Set drawing units to Architectural
- Precision: 1/16"
- Insertion scale: Inches
- Angle type: Decimal Degrees
- Angle precision: 0
- Set lineweight display on
- Set drawing limits to a reasonable residential workspace, for example:
  - lower left: 0,0
  - upper right: 200',200'
- Include a note that model geometry must always be drawn full scale in model space

B. Core NCS-style layer structure
Prepare a layer setup that uses a practical NCS/UDS-inspired naming system for residential architectural work. At minimum include these layers with sensible defaults for color, linetype, lineweight, and plotting behavior:

Architectural:
- A-WALL
- A-DOOR
- A-WIND
- A-FLOR
- A-CLNG
- A-ROOF
- A-STRS
- A-FURN
- A-GLAZ
- A-COLS
- A-HATCH
- A-VIEW

Annotation:
- A-ANNO-DIMS
- A-ANNO-TEXT
- A-ANNO-SYMB

Structural:
- S-BEAM
- S-COLS

Coordination:
- C-GRID

Viewport / non-plot support:
- V-VPRT (must be non-plot)
- DEFPOINTS should be left as system-managed, not recreated

Use a consistent standards-minded property assignment. A reasonable starting point is:
- Walls / major cut elements heavier
- Doors / windows / stairs medium
- annotation light
- hatch very light
- grid medium-light with center linetype
- ceiling on hidden linetype
Document all chosen properties in a separate layer schedule file.

C. Linetypes
Load and use, if available:
- Continuous
- Hidden
- Center
- Phantom
If loading linetypes cannot be fully automated in a reliable way for Mac, document manual steps clearly.

D. Text styles
Target these text styles:
- ANNO-TEXT
- ANNO-TITLE

Use simple professional sans-serif fonts appropriate for architectural work on Mac, but do not hardcode a font that may not exist unless you also provide a fallback strategy. If font assignment is not safely automatable across systems, note manual attention required.

E. Dimension style
Define one base dimension style:
- ARCH-DIMS
Desired behavior:
- architectural units
- precision 1/16"
- text style ANNO-TEXT
- arrow size 1/8"
- text height 3/32"
- readable offsets and spacing suitable for residential documentation
If creation of the dimstyle cannot be fully scripted reliably on Mac, create the best automation possible and list manual completion steps.

F. Annotation scales
Prepare a recommended annotation scale list that includes:
- 1/8" = 1'-0"
- 3/16" = 1'-0"
- 1/4" = 1'-0"
- 1/2" = 1'-0"
- 3/4" = 1'-0"
- 1" = 1'-0"
If scale list editing cannot be fully automated, provide manual instructions and any partial automation available.

G. Model space organization guidance
Include written guidance inside the package explaining:
- all geometry drawn 1:1 in model space
- plans kept near origin
- if multiple floors are kept in one DWG, they should be spatially separated in a disciplined way
- recommendation on when to use one DWG versus separate DWGs with Xrefs
This can be documentation rather than drawing automation.

H. Layouts and sheets
If layout creation is scriptable, create starter layouts. At minimum include:
- one general starter layout for 24x36 ARCH D
- optionally sample named layouts such as:
  - A001-Cover
  - A101-FloorPlan
The layouts should be prepared for paper space use. If page setups, printers, CTB/STB assignments, or PDF devices are machine-dependent and not safely portable, leave placeholders and call them out as manual tasks.

I. Title block guidance
Do not fabricate a final title block graphic unless specifically asked. Instead:
- create a title block requirements document
- specify required fields:
  project name
  client
  project address
  sheet number
  sheet title
  scale
  date
  drawn by
  checked by
  revisions
- note what is best created manually in AutoCAD or from an office standard block library

J. Plotting and standards notes
Document plotting assumptions:
- intended sheet size: ARCH D 24x36 unless otherwise noted
- monochrome plotting preferred unless office standard differs
- viewports should be placed on V-VPRT and set to non-plot
- lineweight hierarchy should support professional black-and-white plotting
Be careful not to claim you can generate portable plot-style files if that is not realistic in this environment.

Expected work product structure:
Create a folder structure like this:

/NCS_Residential_Template_Setup/
  README.md
  TEMPLATE_SPEC.md
  LAYER_SCHEDULE.csv
  SETUP_SCRIPT.scr
  OPTIONAL_AUTOLISP.lsp
  MANUAL_ACTIONS_CHECKLIST.md
  VALIDATION_CHECKLIST.md
  ASSUMPTIONS_AND_LIMITATIONS.md

Content expectations for each file:

README.md
- Explain what the package does
- List files included
- Explain how to use the script in AutoCAD for Mac
- Explain what happens automatically versus manually
- Include a recommended sequence of execution

TEMPLATE_SPEC.md
- Describe the intended final state of the template
- Include all layers, styles, scales, layout expectations, plotting assumptions, and organization rules
- Be explicit about NCS-inspired naming logic and what is intentionally simplified for residential use

LAYER_SCHEDULE.csv
Columns should include at least:
- Layer Name
- Discipline
- Major Group
- Description
- Color
- Linetype
- Lineweight_mm
- Plot
- Notes

SETUP_SCRIPT.scr
- Attempt to automate as much of the drawing setup as possible
- Include commands in a sequence that is realistic for AutoCAD script execution
- Add comments outside the script file where needed, since script comment behavior may be limited
- Be conservative and avoid fragile command flows that are likely to break on Mac
- If command prompts are version-sensitive, document that clearly

OPTIONAL_AUTOLISP.lsp
- Only include if it genuinely improves automation and is likely to work on AutoCAD for Mac
- Use it for repetitive layer creation or variable setup if appropriate
- Keep it readable, well commented, and minimal
- Do not include it if it adds more risk than value

MANUAL_ACTIONS_CHECKLIST.md
- List every item that may still require direct user action in AutoCAD for Mac
- Separate into:
  1. likely automatable but version-sensitive
  2. requires manual UI work
  3. recommended judgment calls by the user
- Include exact commands and where to click when known

VALIDATION_CHECKLIST.md
- Provide a final QA list to confirm:
  - units are correct
  - layer names and properties are correct
  - linetypes loaded
  - text styles present
  - dimstyle present and correct
  - lineweight display is on
  - layout/viewports behave correctly
  - non-plot viewport layer is configured
  - template is ready to save as DWT

ASSUMPTIONS_AND_LIMITATIONS.md
- State what was assumed about AutoCAD for Mac capabilities
- State what could not be confirmed
- State what should be tested before office-wide adoption

Best-practice requirements:
- Favor a lean, professional starting template, not a bloated one
- Keep layer naming standardized and scalable
- Avoid office-specific guesswork unless clearly labeled as a recommendation
- Distinguish between drawing content and template infrastructure
- Preserve flexibility for future Xref-based workflows
- Recommend that sheets and production sheets may eventually be separated from model files for larger projects
- Note that a template should usually contain standards and scaffolding, not project-specific geometry

Automation strategy guidance:
1. Determine what can reasonably be handled by:
   - AutoCAD script (.scr)
   - AutoLISP on AutoCAD for Mac
   - file-based documentation only
2. Implement the automation package accordingly.
3. For every item not automated, add it to the manual checklist with exact follow-up instructions.

Important honesty requirement:
At the end, include a concise “Automation Coverage Summary” that categorizes each template component as:
- Fully automated
- Partially automated
- Manual required
Do not overstate what the automation can do.

When done:
- Present the generated files in full
- Explain how to run them in AutoCAD for Mac
- Explain the manual finish steps in the correct order
- Highlight any commands or script lines that may need adjustment depending on AutoCAD for Mac version

Do not stop at high-level advice. Actually draft the files and contents. Where exact AutoCAD for Mac command scripting is uncertain, provide the best conservative implementation you can and mark uncertain lines with a warning in the documentation instead of silently skipping them.