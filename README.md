# Config Codespace portforwarding for `Streamlit`

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