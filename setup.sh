mkdir -p ~/.streamlit/
echo "\
[general]\n\
email =\"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "1
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
