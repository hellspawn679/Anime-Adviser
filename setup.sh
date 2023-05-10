mkdir -p ~/.streamlit/
echo"\
[server]\n\
port=$PORT\n\
endableCORS=false\n\
headless=true\n\
\n\
" > ~/.stream/config.toml