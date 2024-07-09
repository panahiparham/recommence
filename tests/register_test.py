import numpy as np
from recommence.Checkpoint import Checkpoint


class Agent:
    def __init__(self):
        self.weights = np.zeros((32, 4), dtype=np.float64)
        self.steps = 1

def test_checkpoint_register(tmp_path):
    chk = Checkpoint(save_path=str(tmp_path))

    registered_agent = chk.register('agent', lambda: Agent())

    assert isinstance(registered_agent, Agent)
    assert registered_agent.steps == 1

    chk.save()
    del chk

    chk = Checkpoint(save_path=str(tmp_path))

    loaded_agent = chk['agent']

    assert np.all(loaded_agent.weights == registered_agent.weights)
    assert loaded_agent.steps == registered_agent.steps

    chk.remove()
