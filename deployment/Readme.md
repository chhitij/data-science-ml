### Create virtual envoirnment

- tp create an env --conda create -n <env_name> <python_ver>

- eg conda create -n deployment python==3.7

- conda activate <env_name>

- install flask == > pip install flask

- // conda config --set ssl_verify no

- install sckitlearn -pip install sckit-learn

- conda env list // getting all the envoirnment

- pip freeze > <fileName>requirment.txt</FileName>

- pip install -r requirment.txt // for saving all the package in other system

// In Falsk is best for micro app personal

// Django is for production app industrial

- for deployment over heuruku
  // Add Procfile - > web:gunicorn app:main

  - web: guincorn == > networking stuff
  - app:main --> pthon main.py Pass (platform depended)

  install gunicorn in your env
  create a requirement .txt file
  create a file called Procfile
  upload all files over github
