#!/bin/bash
cd /home/kavia/workspace/code-generation/eventapi-hub-61537-400d62c6/event_manager_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

