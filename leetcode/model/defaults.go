package model

var ConfigDefault = &Config{
	BaseUrl:         "https://leetcode.com",
	SubmissionsDir:  "submissions",
	SubmissionsFile: "submissions.json",
	Offset:          0,
	Limit:           20,
	Action:          CliAction_DOWNLOAD,
}
