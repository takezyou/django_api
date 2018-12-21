'use strict';


/**
 * 写真の保存
 * 投稿の写真とプロフィールの写真を保存することができる
 *
 * body ImagePost base64のコードとカテゴリとポストID
 * no response value expected for this operation
 **/
exports.imagePost = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * ログイン
 * ログインしてトークンを発行する
 *
 * body Login ログインに必要な情報を入力
 * no response value expected for this operation
 **/
exports.login = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * ログアウト
 * ログアウトする
 *
 * no response value expected for this operation
 **/
exports.logout = function() {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * 投稿の削除
 * 自分が投稿した短文を削除する機能(論理削除)
 *
 * body_id Long 投稿のID
 * returns List
 **/
exports.postDelete = function(body_id) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "is_deleted" : false,
  "id" : 1,
  "body" : "fix text"
}, {
  "is_deleted" : false,
  "id" : 1,
  "body" : "fix text"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * 投稿の一覧
 * 自分以外のすべてのユーザーの投稿を時系列順に見る機能
 *
 * no response value expected for this operation
 **/
exports.postList = function() {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * 投稿修正と公開
 * 自分が投稿した短文の内容を修正することと公開することができる
 *
 * body_id Long 投稿のID
 * body PostPatch bodyの修正したものを送る
 * no response value expected for this operation
 **/
exports.postPatch = function(body_id,body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * 投稿
 * 140文字以内の短文を投稿することができる
 *
 * body PostPost 投稿に必要なパラメーターを与える
 * no response value expected for this operation
 **/
exports.postpost = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * ユーザー登録
 * ユーザーの登録をすることができる
 *
 * body Singup ユーザー登録に必要な情報を加える
 * returns SingupResponse
 **/
exports.signup = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "profile" : "profile",
  "email" : "akita@akita.com",
  "username" : "akita"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

