# 🚀 Config Codespace

+ Create codespace on main 
+ `4-core • 8GB RAM • 32GB` (free for personal use)

#### 1. Install and run
```
$ pip install -r requirements.txt
$ streamlit run app.py
```

#### 2. Configure ports
Go to `PORTS` tab in codespace (open new terminal `ctrl + shift + '`)
* Port should open automatically 
* Visibility either public or private


# Codespace Portforwarding for `Streamlit`

* Loading page is stuck on load?

Try adding
```
[server]
enableCORS=false
```
in your `~/.streamlit/config.toml` ([streamlit forum](https://discuss.streamlit.io/t/ec2-streamlit-stuck-on-loading-screen-while-running-streamlit-hello/276))

Create config in codespace
```
mkdir .streamlit
touch .streamlit/config.toml
```
Then add the code snippet above.


# 👀 Github `Dev` Spaces
Press dot `.` on any page on `github.com` to be taken to `github.dev/*`
* Browse and `edit` files
* Commit and `push changes`
* Create `pull requests` 

> **Dev spaces** are good for viewing and quick edits  
> **Codespaces** are virtual VMs linked to your repo

# 💾 Dataframe with editable cells
Creating a dataframe app by [CharlyWargnier](https://github.com/streamlit/example-app-editable-dataframe) and [Pablo Fonseca](https://github.com/PablocFonseca).  
1. Add `streamlit-aggrid==0.2.2-2` to requirements file

# Devcontainers
[documentation link](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers#using-a-predefined-dev-container-configuration)  
Access the Visual Studio Code Command Palette (`Shift + Command + P` / `Ctrl + Shift + P`), then start typing "dev container". Select  
> **Codespaces: Add Development Container Configuration Files...**

* Choose `conda` prebuilt devspace

Add commands to `.devcontainer/devcontainer.json` like
```
"postCreateCommand": "pip3 install --user -r requirements.txt"
```
### To Rebuild Codespace
Access the Visual Studio Code Command Palette (`Ctrl + Shift + P`) then start typing 
> **rebuild**