'use strict';

var utils = require('../utils/writer.js');
var Api = require('../service/ApiService');

module.exports.imagePost = function imagePost (req, res, next) {
  var body = req.swagger.params['body'].value;
  Api.imagePost(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.login = function login (req, res, next) {
  var body = req.swagger.params['body'].value;
  Api.login(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.logout = function logout (req, res, next) {
  Api.logout()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postDelete = function postDelete (req, res, next) {
  var body_id = req.swagger.params['body_id'].value;
  Api.postDelete(body_id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postList = function postList (req, res, next) {
  Api.postList()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postPatch = function postPatch (req, res, next) {
  var body_id = req.swagger.params['body_id'].value;
  var body = req.swagger.params['body'].value;
  Api.postPatch(body_id,body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.postpost = function postpost (req, res, next) {
  var body = req.swagger.params['body'].value;
  Api.postpost(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.signup = function signup (req, res, next) {
  var body = req.swagger.params['body'].value;
  Api.signup(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
