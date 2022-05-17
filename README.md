# 🚀 Config Codespace

+ Create codespace on main (free tier for personal use)
+ `4-core • 8GB RAM • 32GB` 

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