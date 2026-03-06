# week_2
week 2 repo
have added learning 1 folder which isnt releated to mini project and just for my trial.

task_project -- 2nd week weekly mini project.


task_project/
├── .venv/                  # Your isolated Python environment
├── routers/
│   └── task_router.py      # The Waiter (Handles HTTP requests & web traffic)
├── schemas/
│   └── task_schema.py      # The Bouncer (Validates data using Pydantic)
├── services/
│   └── task_service.py     # The Kitchen (Handles the dictionary database & pure logic)
├── main.py                 # The Front Door (Plugs everything together and starts the server)
├── pyproject.toml          # Your project settings and dependencies (managed by uv)
└── README.md               # Your project documentation