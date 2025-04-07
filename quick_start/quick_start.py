import omnigibson as og
from omnigibson.macros import gm

cfg = dict()

# Define scene
cfg["scene"] = {
    "type": "Scene",
    "floor_plane_visible": True,
}

# Define objects
cfg["objects"] = [
    {
        "type": "USDObject",
        "name": "ghost_stain",
        "usd_path": f"{gm.ASSET_PATH}/models/stain/stain.usd",
        "category": "stain",
        "visual_only": True,
        "scale": [1.0, 1.0, 1.0],
        "position": [1.0, 2.0, 0.001],
        "orientation": [0, 0, 0, 1.0],
    },
    {
        "type": "USDObject",
        "name": "hammer",
        "usd_path": f"/home/cy/桌面/Rekep/hammer_description.usd",
        "category": "stain",
        "visual_only": True,
        "scale": [10.0, 10.0, 10.0],
        "position": [1.0, 2.0, 0.001],
        "orientation": [0, 0, 0, 1.0],
    },
    {
        "type": "DatasetObject",
        "name": "delicious_apple",
        "category": "apple",
        "model": "agveuv",
        "position": [0, 0, 1.0],
    },
    {
        "type": "PrimitiveObject",
        "name": "incredible_box",
        "primitive_type": "Cube",
        "rgba": [0, 1.0, 1.0, 1.0],
        "scale": [0.5, 0.5, 0.1],
        "fixed_base": True,
        "position": [-1.0, 0, 1.0],
        "orientation": [0, 0, 0.707, 0.707],
    },
    {
        "type": "LightObject",
        "name": "brilliant_light",
        "light_type": "Sphere",
        "intensity": 50000,
        "radius": 0.1,
        "position": [3.0, 3.0, 4.0],
    },
]

# Define robots
cfg["robots"] = [
    {
        "type": "Fetch",
        "name": "skynet_robot",
        "obs_modalities": ["scan", "rgb", "depth"],
    },
]

# Define task
cfg["task"] = {
    "type": "DummyTask",
    "termination_config": dict(),
    "reward_config": dict(),
}

# Create the environment
env = og.Environment(cfg)

# Allow camera teleoperation
og.sim.enable_viewer_camera_teleoperation()

# Step!
for _ in range(10000):
    obs, rew, terminated, truncated, info = env.step(env.action_space.sample())

og.shutdown()