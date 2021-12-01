
year=${1:-2021}
day=${2?Error: needs day}
mkdir Python/$year/day\ $day/

cp template.py Python/$year/day\ $day/$day.py
python3.9 get_input.py $day $year > Python/$year/day\ $day/$day.in
cd Python/$year/day\ $day
echo "$year, $day"
