import speedtest

st = speedtest.Speedtest()
option = int(input('''What speed do you want to test:
1) Download Speed
2) Upload Speed
3) Ping
Your Choice: '''))

if option == 1:
    download_speed = st.download() / 10**6
    print(f"Download Speed: {download_speed:.2f} Mbps")
elif option == 2:
    upload_speed = st.upload() / 10**6
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    ping_result = st.results.ping
    print(f"Ping: {ping_result:.2f} ms")
else:
    print("Please enter the correct choice !")
