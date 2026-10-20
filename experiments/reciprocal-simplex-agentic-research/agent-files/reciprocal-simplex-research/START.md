# Start a research run

Open this folder as the Codex working project, choose GPT-5.6 Sol, and send:

> Run the research workflow in this folder using subagents. Read AGENTS.md,
> workflow.json and instructions/coordinator.md. Use gpt-5.6-sol with xhigh
> reasoning for the coordinator and every agent. Use one literature agent,
> five independent proof approaches, the critical reviewer and the coder as
> needed. The target is the exact problem in common/problem_statement.md,
> including prescribed intensity. Initialize a new run, freeze common inputs,
> keep separate contexts, and obtain an extensive final review report. Do not
> replace the exact target with an approximation or an empirical fit. Work
> through the configured review rounds and report remaining gaps honestly.
> Record per-agent wall time and every runtime-exposed input, cached-input,
> output, reasoning and total token count in agent_accounting.md. Include
> structured reasoning summaries, not raw private chain-of-thought.

This prompt starts model work only when you send it. Saving this file or opening
the folder does not start the research.
