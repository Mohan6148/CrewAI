from .llm import LLM


class Agent:
    def __init__(self, role, goal, backstory, memory=False, verbose=False, llm=None, **kwargs):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.memory = memory
        self.verbose = verbose
        self.llm = llm


class Task:
    def __init__(self, description, expected_output, agent, **kwargs):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent


class Crew:
    def __init__(self, agents, tasks, verbose=False, **kwargs):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose

    def kickoff(self):
        outputs = []
        previous_output = ""

        for task in self.tasks:
            agent = task.agent
            if agent.llm is None:
                raise RuntimeError(f"No LLM configured for agent {agent.role}")

            prompt = (
                f"You are {agent.role}.\n"
                f"Goal: {agent.goal}\n"
                f"Backstory: {agent.backstory}\n\n"
                f"Task: {task.description}\n"
                f"Expected output: {task.expected_output}\n"
            )
            if previous_output:
                prompt += f"\nPrevious agent output:\n{previous_output}\n"

            result = agent.llm.generate(prompt)
            outputs.append(f"[{agent.role}]\n{result}")
            previous_output = result

        return "\n\n".join(outputs)
