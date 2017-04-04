var webpack = require('webpack');
var path = require('path');

module.exports = {
	context: __dirname + "/scripts",
	entry: "./main.ts",
	output: {
		path: __dirname + "/dist",
		filename: "bundle.js"
	},
	plugins: [
		//new webpack.optimize.UglifyJsPlugin({mangle: false})
	],
	target: 'web',
	module: {
		loaders: [
			{ 
				test: /\.tsx?$/, 
				loader: "ts-loader" 
			}
		]
	}
};