# Config Codespace

+ Create codespace on main (free tier for personal use)
+ `4-core • 8GB RAM • 32GB` 

### Install and run
```
$ pip install -r requirements.txt
$ streamlit run app.py
```

# Codespace Portforwarding for `Streamlit`

* Loading page is stuck on load?

Try adding 
```
[server]
enableCORS=false
```
in your `~/.streamlit/config.toml` ([streamlit forum](https://discuss.streamlit.io/t/ec2-streamlit-stuck-on-loading-screen-while-running-streamlit-hello/276))

Then
```
$ streamlit hello
```