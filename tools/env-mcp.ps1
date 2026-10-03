$Scripts = "C:\Users\tusen\AppData\Local\Python\pythoncore-3.14-64\Scripts"

$userPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ($userPath -notlike "*$Scripts*") {
    [Environment]::SetEnvironmentVariable(
        "Path",
        ($userPath.TrimEnd(";") + ";" + $Scripts),
        "User"
    )
}

$env:Path += ";$Scripts"
