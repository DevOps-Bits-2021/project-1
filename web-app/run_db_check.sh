#!/bin/bash

if [[ -f app.db ]]; then
  flask db migrate
  flask db upgrade
else
  if [[ -d migrations ]]; then
    flask db migrate
    flask db upgrade
  else
    flask db init
    flask db migrate
    flask db upgrade
  fi
fi
