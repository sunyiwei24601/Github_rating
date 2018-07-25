# Github API使用指南

## Authorization

### 私有token

`` curl -i -H 'Authorization: token 03de74ada736153e374e5a9efb979c361c36463c' https://api.github.com/user/starred ``

利用headers和token

``curl -u sunyiwei24601:03de74ada736153e374e5a9efb979c361c36463c https://api.github.com/users/technoweenie/repos?type=owner``

用户名：token

## 查询功能

​	Github文档写的倒是挺好的，数据也很完整，功能也很多，但是坑爹是这个references的顺序居然是按照首字母排序的！！！建议新手阅读的时候，从repository开始阅读，然后projects，issues，reactions，activities，就可以更加舒服一点。

### Profile

直接搜索'/users/username'可以获得许多信息

![1529922169682](1529922169682.png)



这些很多也是后面要介绍的内容

### Events

Events support [pagination](https://developer.github.com/v3/#pagination), however the `per_page` option is unsupported. The fixed page size is 30 items. Fetching up to ten pages is supported, for a total of 300 events.

Only events created within the past 90 days will be included in timelines. Events older than 90 days will not be included (even if the total number of events in the timeline is less than 300).

具体的总页数和数量以及下一页的信息都在headers当中，当然也可以选择？page=num来完成这样的查询操作，后续所有的查询操作都是支持这样的sort操作的。

#### public events

`` GET /users/username/events``

![1529922903398](1529922903398.png)

所有得到的都形如以上event类型，目标，repository具体的内容和时间都会标注在event里

#### repository events

`` GET /repos/:owner/:repo/events``

``GET /repos/:owner/:repo/issues/events``

#### List public events for a network of repositories

``GET /networks/:owner/:repo/events``

``GET /orgs/:org/events``

#### Event Types

- [CheckRunEvent](https://developer.github.com/v3/activity/events/types/#checkrunevent)
- [CheckSuiteEvent](https://developer.github.com/v3/activity/events/types/#checksuiteevent)
- [CommitCommentEvent](https://developer.github.com/v3/activity/events/types/#commitcommentevent)
- [CreateEvent](https://developer.github.com/v3/activity/events/types/#createevent)
- [DeleteEvent](https://developer.github.com/v3/activity/events/types/#deleteevent)
- [DeploymentEvent](https://developer.github.com/v3/activity/events/types/#deploymentevent)
- [DeploymentStatusEvent](https://developer.github.com/v3/activity/events/types/#deploymentstatusevent)
- [DownloadEvent](https://developer.github.com/v3/activity/events/types/#downloadevent)
- [FollowEvent](https://developer.github.com/v3/activity/events/types/#followevent)
- [ForkEvent](https://developer.github.com/v3/activity/events/types/#forkevent)
- [ForkApplyEvent](https://developer.github.com/v3/activity/events/types/#forkapplyevent)
- [GistEvent](https://developer.github.com/v3/activity/events/types/#gistevent)
- [GollumEvent](https://developer.github.com/v3/activity/events/types/#gollumevent)
- [InstallationEvent](https://developer.github.com/v3/activity/events/types/#installationevent)
- [InstallationRepositoriesEvent](https://developer.github.com/v3/activity/events/types/#installationrepositoriesevent)
- [IssueCommentEvent](https://developer.github.com/v3/activity/events/types/#issuecommentevent)
- [IssuesEvent](https://developer.github.com/v3/activity/events/types/#issuesevent)
- [LabelEvent](https://developer.github.com/v3/activity/events/types/#labelevent)
- [MarketplacePurchaseEvent](https://developer.github.com/v3/activity/events/types/#marketplacepurchaseevent)
- [MemberEvent](https://developer.github.com/v3/activity/events/types/#memberevent)
- [MembershipEvent](https://developer.github.com/v3/activity/events/types/#membershipevent)
- [MilestoneEvent](https://developer.github.com/v3/activity/events/types/#milestoneevent)
- [OrganizationEvent](https://developer.github.com/v3/activity/events/types/#organizationevent)
- [OrgBlockEvent](https://developer.github.com/v3/activity/events/types/#orgblockevent)
- [PageBuildEvent](https://developer.github.com/v3/activity/events/types/#pagebuildevent)
- [ProjectCardEvent](https://developer.github.com/v3/activity/events/types/#projectcardevent)
- [ProjectColumnEvent](https://developer.github.com/v3/activity/events/types/#projectcolumnevent)
- [ProjectEvent](https://developer.github.com/v3/activity/events/types/#projectevent)
- [PublicEvent](https://developer.github.com/v3/activity/events/types/#publicevent)
- [PullRequestEvent](https://developer.github.com/v3/activity/events/types/#pullrequestevent)
- [PullRequestReviewEvent](https://developer.github.com/v3/activity/events/types/#pullrequestreviewevent)
- [PullRequestReviewCommentEvent](https://developer.github.com/v3/activity/events/types/#pullrequestreviewcommentevent)
- [PushEvent](https://developer.github.com/v3/activity/events/types/#pushevent)
- [ReleaseEvent](https://developer.github.com/v3/activity/events/types/#releaseevent)
- [RepositoryEvent](https://developer.github.com/v3/activity/events/types/#repositoryevent)
- [RepositoryVulnerabilityAlertEvent](https://developer.github.com/v3/activity/events/types/#repositoryvulnerabilityalertevent)
- [StatusEvent](https://developer.github.com/v3/activity/events/types/#statusevent)
- [TeamEvent](https://developer.github.com/v3/activity/events/types/#teamevent)
- [TeamAddEvent](https://developer.github.com/v3/activity/events/types/#teamaddevent)
- [WatchEvent](https://developer.github.com/v3/activity/events/types/#watchevent)

### Feeds

展示授权用户目前接收到的feeds

### Starring

`` GET /repos/:owner/:repo/stargazers``

#### List repositories being starred

``GET /users/:username/starred``

| Name        | Type     | Description                                                  |
| ----------- | -------- | ------------------------------------------------------------ |
| `sort`      | `string` | One of `created` (when the repository was starred) or `updated` (when it was last pushed to). Default: `created` |
| `direction` | `string` | One of `asc` (ascending) or `desc` (descending). Default: `desc` |

``Accept: application/vnd.github.v3.star+json``

添加以上headers可以得到很好的效果

### Watching

#### List Watchers

``GET /repos/:owner/:repo/subscribers``

#### List repositories being watched

```
GET /users/:username/subscriptions
```

### Issues

```Get /repos/username/repo/issues```

查看某一项目的issues

![1529982579311](C:\Users\Carl\PycharmProjects\Gitrating\1529982579311.png)

issues都有一个自己的编号，然后有各自的events等，通过加上/编号得到具体的信息

#### List comments in a repository

```
GET /repos/:owner/:repo/issues/comments
```

得到某个特定的comments

```
GET /repos/:owner/:repo/issues/comments/:comment_id
```

#### Reactions

issues的查询操作都可以加上reactions来查看点赞支持反对等具体的内容，不过headers的Accept要加上

```
  application/vnd.github.squirrel-girl-preview
```

```json
{
  "total_count": 5,
  "+1": 3,
  "-1": 1,
  "laugh": 0,
  "confused": 0,
  "heart": 1,
  "hooray": 0,
  "url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1/reactions"
}
```

- [Reaction types](https://developer.github.com/v3/reactions/#reaction-types)
- [List reactions for a commit comment](https://developer.github.com/v3/reactions/#list-reactions-for-a-commit-comment)
- [Create reaction for a commit comment](https://developer.github.com/v3/reactions/#create-reaction-for-a-commit-comment)
- [List reactions for an issue](https://developer.github.com/v3/reactions/#list-reactions-for-an-issue)
- [Create reaction for an issue](https://developer.github.com/v3/reactions/#create-reaction-for-an-issue)
- [List reactions for an issue comment](https://developer.github.com/v3/reactions/#list-reactions-for-an-issue-comment)
- [Create reaction for an issue comment](https://developer.github.com/v3/reactions/#create-reaction-for-an-issue-comment)
- [List reactions for a pull request review comment](https://developer.github.com/v3/reactions/#list-reactions-for-a-pull-request-review-comment)
- [Create reaction for a pull request review comment](https://developer.github.com/v3/reactions/#create-reaction-for-a-pull-request-review-comment)
- [List reactions for a team discussion](https://developer.github.com/v3/reactions/#list-reactions-for-a-team-discussion)
- [Create reaction for a team discussion](https://developer.github.com/v3/reactions/#create-reaction-for-a-team-discussion)
- [List reactions for a team discussion comment](https://developer.github.com/v3/reactions/#list-reactions-for-a-team-discussion-comment)
- [Create reaction for a team discussion comment](https://developer.github.com/v3/reactions/#create-reaction-for-a-team-discussion-comment)
- [Delete a reaction](https://developer.github.com/v3/reactions/#delete-a-reaction)
