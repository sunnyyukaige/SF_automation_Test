cd $pwd
$excuteTool='./UI-automation-classical'
$reportPath='./Result/'
echo "the environment for run is " + $args[0]
cd $excuteTool
if(Test-path $reportPath){
remove-item $reportPath/* 
echo 'sunnytest'
}
else{
New-Item -Path $reportPath -ItemType directory
}
   & cd $excuteTool 
   & behave  -D env=$args[0] -D browser='chrome' --junit --junit-directory $reportPath



