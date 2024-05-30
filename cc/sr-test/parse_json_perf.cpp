#include <benchmark/benchmark.h>

#include <cstring>
#include <iostream>
#include <vector>

#include "exprs/jsonpath.h"
#include "json_converter.cpp"
#include "util/json.h"
#include "util/slice.h"

using namespace starrocks;

// const char* github_event_json0 = R"({"a":10})";

const char* github_event_json0 = R"({
    "id": "1978774738",
    "type": "PullRequestEvent",
    "actor": {
      "id": 3286055,
      "login": "shutter111",
      "gravatar_id": "529cf44876fe50fee32f301edb6f6c61",
      "url": "https://api.github.com/users/shutter111",
      "avatar_url": "https://gravatar.com/avatar/529cf44876fe50fee32f301edb6f6c61?d=https%3A%2F%2Fa248.e.akamai.net%2Fassets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&r=x"
    },
    "repo": {
      "id": 12934800,
      "name": "RichmondDay/www.mini.ca",
      "url": "https://api.github.com/repos/RichmondDay/www.mini.ca"
    },
    "payload": {
      "action": "opened",
      "number": 363,
      "pull_request": {
        "url": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls/363",
        "id": 12494789,
        "html_url": "https://github.com/RichmondDay/www.mini.ca/pull/363",
        "diff_url": "https://github.com/RichmondDay/www.mini.ca/pull/363.diff",
        "patch_url": "https://github.com/RichmondDay/www.mini.ca/pull/363.patch",
        "issue_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/issues/363",
        "number": 363,
        "state": "open",
        "title": "updated mobile detect",
        "user": {
          "login": "shutter111",
          "id": 3286055,
          "avatar_url": "https://gravatar.com/avatar/529cf44876fe50fee32f301edb6f6c61?d=https%3A%2F%2Fidenticons.github.com%2F2d02137248eabfa86a9fa3c5161e5218.png&r=x",
          "gravatar_id": "529cf44876fe50fee32f301edb6f6c61",
          "url": "https://api.github.com/users/shutter111",
          "html_url": "https://github.com/shutter111",
          "followers_url": "https://api.github.com/users/shutter111/followers",
          "following_url": "https://api.github.com/users/shutter111/following{/other_user}",
          "gists_url": "https://api.github.com/users/shutter111/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/shutter111/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/shutter111/subscriptions",
          "organizations_url": "https://api.github.com/users/shutter111/orgs",
          "repos_url": "https://api.github.com/users/shutter111/repos",
          "events_url": "https://api.github.com/users/shutter111/events{/privacy}",
          "received_events_url": "https://api.github.com/users/shutter111/received_events",
          "type": "User",
          "site_admin": false
        },
        "body": "",
        "created_at": "2014-02-13T03:20:35Z",
        "updated_at": "2014-02-13T03:20:35Z",
        "closed_at": null,
        "merged_at": null,
        "merge_commit_sha": null,
        "assignee": null,
        "milestone": null,
        "commits_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls/363/commits",
        "review_comments_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls/363/comments",
        "review_comment_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls/comments/{number}",
        "comments_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/issues/363/comments",
        "statuses_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/statuses/8753c6bb03bfdbc1692ddd84cf12a3f61ceedfef",
        "head": {
          "label": "shutter111:master",
          "ref": "master",
          "sha": "8753c6bb03bfdbc1692ddd84cf12a3f61ceedfef",
          "user": {
            "login": "shutter111",
            "id": 3286055,
            "avatar_url": "https://gravatar.com/avatar/529cf44876fe50fee32f301edb6f6c61?d=https%3A%2F%2Fidenticons.github.com%2F2d02137248eabfa86a9fa3c5161e5218.png&r=x",
            "gravatar_id": "529cf44876fe50fee32f301edb6f6c61",
            "url": "https://api.github.com/users/shutter111",
            "html_url": "https://github.com/shutter111",
            "followers_url": "https://api.github.com/users/shutter111/followers",
            "following_url": "https://api.github.com/users/shutter111/following{/other_user}",
            "gists_url": "https://api.github.com/users/shutter111/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/shutter111/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/shutter111/subscriptions",
            "organizations_url": "https://api.github.com/users/shutter111/orgs",
            "repos_url": "https://api.github.com/users/shutter111/repos",
            "events_url": "https://api.github.com/users/shutter111/events{/privacy}",
            "received_events_url": "https://api.github.com/users/shutter111/received_events",
            "type": "User",
            "site_admin": false
          },
          "repo": {
            "id": 13094898,
            "name": "www.mini.ca",
            "full_name": "shutter111/www.mini.ca",
            "owner": {
              "login": "shutter111",
              "id": 3286055,
              "avatar_url": "https://gravatar.com/avatar/529cf44876fe50fee32f301edb6f6c61?d=https%3A%2F%2Fidenticons.github.com%2F2d02137248eabfa86a9fa3c5161e5218.png&r=x",
              "gravatar_id": "529cf44876fe50fee32f301edb6f6c61",
              "url": "https://api.github.com/users/shutter111",
              "html_url": "https://github.com/shutter111",
              "followers_url": "https://api.github.com/users/shutter111/followers",
              "following_url": "https://api.github.com/users/shutter111/following{/other_user}",
              "gists_url": "https://api.github.com/users/shutter111/gists{/gist_id}",
              "starred_url": "https://api.github.com/users/shutter111/starred{/owner}{/repo}",
              "subscriptions_url": "https://api.github.com/users/shutter111/subscriptions",
              "organizations_url": "https://api.github.com/users/shutter111/orgs",
              "repos_url": "https://api.github.com/users/shutter111/repos",
              "events_url": "https://api.github.com/users/shutter111/events{/privacy}",
              "received_events_url": "https://api.github.com/users/shutter111/received_events",
              "type": "User",
              "site_admin": false
            },
            "private": false,
            "html_url": "https://github.com/shutter111/www.mini.ca",
            "description": "www.mini.ca",
            "fork": true,
            "url": "https://api.github.com/repos/shutter111/www.mini.ca",
            "forks_url": "https://api.github.com/repos/shutter111/www.mini.ca/forks",
            "keys_url": "https://api.github.com/repos/shutter111/www.mini.ca/keys{/key_id}",
            "collaborators_url": "https://api.github.com/repos/shutter111/www.mini.ca/collaborators{/collaborator}",
            "teams_url": "https://api.github.com/repos/shutter111/www.mini.ca/teams",
            "hooks_url": "https://api.github.com/repos/shutter111/www.mini.ca/hooks",
            "issue_events_url": "https://api.github.com/repos/shutter111/www.mini.ca/issues/events{/number}",
            "events_url": "https://api.github.com/repos/shutter111/www.mini.ca/events",
            "assignees_url": "https://api.github.com/repos/shutter111/www.mini.ca/assignees{/user}",
            "branches_url": "https://api.github.com/repos/shutter111/www.mini.ca/branches{/branch}",
            "tags_url": "https://api.github.com/repos/shutter111/www.mini.ca/tags",
            "blobs_url": "https://api.github.com/repos/shutter111/www.mini.ca/git/blobs{/sha}",
            "git_tags_url": "https://api.github.com/repos/shutter111/www.mini.ca/git/tags{/sha}",
            "git_refs_url": "https://api.github.com/repos/shutter111/www.mini.ca/git/refs{/sha}",
            "trees_url": "https://api.github.com/repos/shutter111/www.mini.ca/git/trees{/sha}",
            "statuses_url": "https://api.github.com/repos/shutter111/www.mini.ca/statuses/{sha}",
            "languages_url": "https://api.github.com/repos/shutter111/www.mini.ca/languages",
            "stargazers_url": "https://api.github.com/repos/shutter111/www.mini.ca/stargazers",
            "contributors_url": "https://api.github.com/repos/shutter111/www.mini.ca/contributors",
            "subscribers_url": "https://api.github.com/repos/shutter111/www.mini.ca/subscribers",
            "subscription_url": "https://api.github.com/repos/shutter111/www.mini.ca/subscription",
            "commits_url": "https://api.github.com/repos/shutter111/www.mini.ca/commits{/sha}",
            "git_commits_url": "https://api.github.com/repos/shutter111/www.mini.ca/git/commits{/sha}",
            "comments_url": "https://api.github.com/repos/shutter111/www.mini.ca/comments{/number}",
            "issue_comment_url": "https://api.github.com/repos/shutter111/www.mini.ca/issues/comments/{number}",
            "contents_url": "https://api.github.com/repos/shutter111/www.mini.ca/contents/{+path}",
            "compare_url": "https://api.github.com/repos/shutter111/www.mini.ca/compare/{base}...{head}",
            "merges_url": "https://api.github.com/repos/shutter111/www.mini.ca/merges",
            "archive_url": "https://api.github.com/repos/shutter111/www.mini.ca/{archive_format}{/ref}",
            "downloads_url": "https://api.github.com/repos/shutter111/www.mini.ca/downloads",
            "issues_url": "https://api.github.com/repos/shutter111/www.mini.ca/issues{/number}",
            "pulls_url": "https://api.github.com/repos/shutter111/www.mini.ca/pulls{/number}",
            "milestones_url": "https://api.github.com/repos/shutter111/www.mini.ca/milestones{/number}",
            "notifications_url": "https://api.github.com/repos/shutter111/www.mini.ca/notifications{?since,all,participating}",
            "labels_url": "https://api.github.com/repos/shutter111/www.mini.ca/labels{/name}",
            "releases_url": "https://api.github.com/repos/shutter111/www.mini.ca/releases{/id}",
            "created_at": "2013-09-25T13:46:25Z",
            "updated_at": "2014-02-13T03:20:35Z",
            "pushed_at": "2014-02-13T03:19:17Z",
            "git_url": "git://github.com/shutter111/www.mini.ca.git",
            "ssh_url": "git@github.com:shutter111/www.mini.ca.git",
            "clone_url": "https://github.com/shutter111/www.mini.ca.git",
            "svn_url": "https://github.com/shutter111/www.mini.ca",
            "homepage": "mini.richmondday.com",
            "size": 696866,
            "stargazers_count": 0,
            "watchers_count": 0,
            "language": "C#",
            "has_issues": false,
            "has_downloads": true,
            "has_wiki": true,
            "forks_count": 0,
            "mirror_url": null,
            "open_issues_count": 0,
            "forks": 0,
            "open_issues": 0,
            "watchers": 0,
            "default_branch": "master",
            "master_branch": "master"
          }
        },
        "base": {
          "label": "RichmondDay:master",
          "ref": "master",
          "sha": "eec54db0bcf7d0e4f498239559e8aa3f234b2d1a",
          "user": {
            "login": "RichmondDay",
            "id": 3278547,
            "avatar_url": "https://gravatar.com/avatar/9e7208e61842f701042e1222865cb8eb?d=https%3A%2F%2Fidenticons.github.com%2Fafc6808062ff145f794691e5f6a9191a.png&r=x",
            "gravatar_id": "9e7208e61842f701042e1222865cb8eb",
            "url": "https://api.github.com/users/RichmondDay",
            "html_url": "https://github.com/RichmondDay",
            "followers_url": "https://api.github.com/users/RichmondDay/followers",
            "following_url": "https://api.github.com/users/RichmondDay/following{/other_user}",
            "gists_url": "https://api.github.com/users/RichmondDay/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/RichmondDay/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/RichmondDay/subscriptions",
            "organizations_url": "https://api.github.com/users/RichmondDay/orgs",
            "repos_url": "https://api.github.com/users/RichmondDay/repos",
            "events_url": "https://api.github.com/users/RichmondDay/events{/privacy}",
            "received_events_url": "https://api.github.com/users/RichmondDay/received_events",
            "type": "Organization",
            "site_admin": false
          },
          "repo": {
            "id": 12934800,
            "name": "www.mini.ca",
            "full_name": "RichmondDay/www.mini.ca",
            "owner": {
              "login": "RichmondDay",
              "id": 3278547,
              "avatar_url": "https://gravatar.com/avatar/9e7208e61842f701042e1222865cb8eb?d=https%3A%2F%2Fidenticons.github.com%2Fafc6808062ff145f794691e5f6a9191a.png&r=x",
              "gravatar_id": "9e7208e61842f701042e1222865cb8eb",
              "url": "https://api.github.com/users/RichmondDay",
              "html_url": "https://github.com/RichmondDay",
              "followers_url": "https://api.github.com/users/RichmondDay/followers",
              "following_url": "https://api.github.com/users/RichmondDay/following{/other_user}",
              "gists_url": "https://api.github.com/users/RichmondDay/gists{/gist_id}",
              "starred_url": "https://api.github.com/users/RichmondDay/starred{/owner}{/repo}",
              "subscriptions_url": "https://api.github.com/users/RichmondDay/subscriptions",
              "organizations_url": "https://api.github.com/users/RichmondDay/orgs",
              "repos_url": "https://api.github.com/users/RichmondDay/repos",
              "events_url": "https://api.github.com/users/RichmondDay/events{/privacy}",
              "received_events_url": "https://api.github.com/users/RichmondDay/received_events",
              "type": "Organization",
              "site_admin": false
            },
            "private": false,
            "html_url": "https://github.com/RichmondDay/www.mini.ca",
            "description": "www.mini.ca",
            "fork": false,
            "url": "https://api.github.com/repos/RichmondDay/www.mini.ca",
            "forks_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/forks",
            "keys_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/keys{/key_id}",
            "collaborators_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/collaborators{/collaborator}",
            "teams_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/teams",
            "hooks_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/hooks",
            "issue_events_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/issues/events{/number}",
            "events_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/events",
            "assignees_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/assignees{/user}",
            "branches_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/branches{/branch}",
            "tags_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/tags",
            "blobs_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/git/blobs{/sha}",
            "git_tags_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/git/tags{/sha}",
            "git_refs_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/git/refs{/sha}",
            "trees_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/git/trees{/sha}",
            "statuses_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/statuses/{sha}",
            "languages_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/languages",
            "stargazers_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/stargazers",
            "contributors_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/contributors",
            "subscribers_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/subscribers",
            "subscription_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/subscription",
            "commits_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/commits{/sha}",
            "git_commits_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/git/commits{/sha}",
            "comments_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/comments{/number}",
            "issue_comment_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/issues/comments/{number}",
            "contents_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/contents/{+path}",
            "compare_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/compare/{base}...{head}",
            "merges_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/merges",
            "archive_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/{archive_format}{/ref}",
            "downloads_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/downloads",
            "issues_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/issues{/number}",
            "pulls_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls{/number}",
            "milestones_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/milestones{/number}",
            "notifications_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/notifications{?since,all,participating}",
            "labels_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/labels{/name}",
            "releases_url": "https://api.github.com/repos/RichmondDay/www.mini.ca/releases{/id}",
            "created_at": "2013-09-18T21:18:08Z",
            "updated_at": "2014-02-13T03:10:42Z",
            "pushed_at": "2014-02-13T03:10:42Z",
            "git_url": "git://github.com/RichmondDay/www.mini.ca.git",
            "ssh_url": "git@github.com:RichmondDay/www.mini.ca.git",
            "clone_url": "https://github.com/RichmondDay/www.mini.ca.git",
            "svn_url": "https://github.com/RichmondDay/www.mini.ca",
            "homepage": "mini.richmondday.com",
            "size": 699142,
            "stargazers_count": 0,
            "watchers_count": 0,
            "language": "C#",
            "has_issues": true,
            "has_downloads": true,
            "has_wiki": true,
            "forks_count": 3,
            "mirror_url": null,
            "open_issues_count": 2,
            "forks": 3,
            "open_issues": 2,
            "watchers": 0,
            "default_branch": "master",
            "master_branch": "master"
          }
        },
        "_links": {
          "self": {
            "href": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls/363"
          },
          "html": {
            "href": "https://github.com/RichmondDay/www.mini.ca/pull/363"
          },
          "issue": {
            "href": "https://api.github.com/repos/RichmondDay/www.mini.ca/issues/363"
          },
          "comments": {
            "href": "https://api.github.com/repos/RichmondDay/www.mini.ca/issues/363/comments"
          },
          "review_comments": {
            "href": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls/363/comments"
          },
          "review_comment": {
            "href": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls/comments/{number}"
          },
          "commits": {
            "href": "https://api.github.com/repos/RichmondDay/www.mini.ca/pulls/363/commits"
          },
          "statuses": {
            "href": "https://api.github.com/repos/RichmondDay/www.mini.ca/statuses/8753c6bb03bfdbc1692ddd84cf12a3f61ceedfef"
          }
        },
        "merged": false,
        "mergeable": null,
        "mergeable_state": "unknown",
        "merged_by": null,
        "comments": 0,
        "review_comments": 0,
        "commits": 1,
        "additions": 28,
        "deletions": 4,
        "changed_files": 1
      }
    },
    "public": true,
    "created_at": "2014-02-13T03:20:35Z",
    "org": {
      "id": 3278547,
      "login": "RichmondDay",
      "gravatar_id": "9e7208e61842f701042e1222865cb8eb",
      "url": "https://api.github.com/orgs/RichmondDay",
      "avatar_url": "https://gravatar.com/avatar/9e7208e61842f701042e1222865cb8eb?d=https%3A%2F%2Fa248.e.akamai.net%2Fassets.github.com%2Fimages%2Fgravatars%2Fgravatar-org-420.png&r=x"
    }
  })";

std::vector<Slice> input_data;

void velocypack_load(const Slice& src, JsonValue& value) {
    Status st = JsonValue::parse(src, &value);
    if (!st.ok()) {
        std::cout << st.message() << "\n";
        return;
    }
}

static void test_velocypack_load(benchmark::State& state) {
    for (auto _ : state) {
        for (const Slice& src : input_data) {
            JsonValue value;
            velocypack_load(src, value);
            benchmark::DoNotOptimize(value);
        }
    }
}

void simdjson_load(const Slice& src, JsonValue& value) {
    simdjson::ondemand::parser _parser;
    std::vector<char> room;
    room.resize(src.size + simdjson::SIMDJSON_PADDING);
    memcpy(room.data(), src.data, src.size);
    simdjson::padded_string_view view(room.data(), src.size, room.size());

    simdjson::ondemand::document _doc = _parser.iterate(view);
    simdjson::ondemand::object row = _doc.get_object();

    benchmark::DoNotOptimize(row);
    StatusOr<JsonValue> st = SimdJsonConverter::create((SimdJsonObject)row);
    if (!st.ok()) {
        std::cout << st.status().message() << "\n";
        return;
    }
    value = std::move(st.value());
}

static void test_simdjson_load(benchmark::State& state) {
    for (auto _ : state) {
        for (const Slice& src : input_data) {
            JsonValue value;
            simdjson_load(src, value);
            benchmark::DoNotOptimize(value);
        }
    }
}

static void test_velocypack_parse_path(benchmark::State& state) {
    const char* path = "$.payload.pull_request.url";
    const Slice slice(path);
    for (auto _ : state) {
        auto res = JsonPath::parse(slice);
        if (!res.ok()) {
            std::cout << res.status().message() << "\n";
            break;
        }
        benchmark::DoNotOptimize(res);
    }
}

BENCHMARK(test_velocypack_load);
BENCHMARK(test_simdjson_load);
BENCHMARK(test_velocypack_parse_path);

int main(int argc, char** argv) {
    // 初始化 Google Benchmark
    benchmark::Initialize(&argc, argv);

    // // 如果只是想列出基准测试，而不运行它们
    // if (benchmark::ReportUnrecognizedArguments(argc, argv)) {
    //     return 1;
    // }

    input_data.emplace_back(github_event_json0);

    bool stats = false;
    if (stats) {
        for (const Slice& x : input_data) {
            JsonValue value;

            velocypack_load(x, value);
            std::cout << "json data = " << value.to_string().value() << "\n";

            simdjson_load(x, value);
            std::cout << "json data = " << value.to_string().value() << "\n";

            std::cout << "json length = " << x.size << "\n";
        }
    }

    if (!stats) {
        // 运行基准测试
        benchmark::RunSpecifiedBenchmarks();
    }
}
