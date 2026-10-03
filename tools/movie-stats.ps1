$data = Import-Csv "$PSScriptRoot\..\movies.csv"

$total = $data.Count
$average = ($data | Measure-Object rating -Average).Average

Write-Output "电影数量: $total"
Write-Output "平均评分: $([math]::Round($average, 2))"
