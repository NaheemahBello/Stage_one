from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
	#Get query parameter
	slack_name = request.args.get('slack_name')
	track = request.args.get('track')

	if track not in ["backend"]:
		return jsonify({"error": "invalid track"}), 400

	#Get current date
	current_day = datetime.datetime.now(pytz.utc).strftime('%A')

	#Get current UTC time
	utc_time = datetime.datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

	#Github Urls
	github_repo_url = (f"https://github.com/NaheemahBello/Stage_one")
	github_file_url = (f"https://github.com/NaheemahBello/Stage_one/blob/main/app.py")

	# Response
	response_data = {
	"slack_name": slack_name,
	"current_day": current_day,
	"utc_time": utc_time,
	"track": track,
	"github_file_url": github_file_url,
	"github_repo_url": github_repo_url,
	"status_code": 200
}

	return jsonify(response_data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
