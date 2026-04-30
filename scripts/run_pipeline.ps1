param(
    [string]$Repo = "examples/sample_repo",
    [string]$Output = "outputs"
)

python -m agents.orchestrator --repo $Repo --output $Output
