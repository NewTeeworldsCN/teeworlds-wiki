# Foot
Foot，即[teefoot(football)](https://github.com/unique-clan/football)，中文俗称“球类运动”，是一款由[unique-clan](https://github.com/unique-clan)团队发起的休闲模式。根据其官方自述文档，该项目目前由开发者 **GreYFoX** (又名 Shereef Marzouk) 负责其重构工作。


## 模式玩法
玩家分为人数均衡的两队进行对抗。每轮游戏开始一段时间后，场上固定区域会刷新出一个可拾取的**榴弹炮**，它在此模式中将作为**“球”**使用。

![球](resources/foot/ball.jpg){.bordered-img tooltip="球"}

玩家触碰后即可拾取球，并可以向任意角度**投出**。

![射出的球](resources/foot/entityball.jpg){.bordered-img tooltip="射出的球"}

成功将球**射入**球门后，即会判定得分并结束本轮，所有玩家将立即重生，准备下一轮对抗。任意一队的分数达到规定分数后本局游戏结束。

### 关于球
当球刷新在场上时，聊天区会显示“**Ball Respawned**（球已刷新）”，此时任何玩家都可将其捡起。持球玩家若长时间未将球**投出**，球将会被自动**投出**（持球者的护盾值即为最大持球时间的倒计时）。持球者重生后，球会自动朝其重生时面向的方向飞出。任何玩家都可以通过**锤击**持球者来**抢断**此球。

![正在抢球的红蓝队玩家](resources/foot/catch.jpg){.bordered-img tooltip="正在抢球的红蓝队玩家"}

若场上的球长时间无人拾取，它会自行消失，并在一段时间后以榴弹炮的形式再次出现在刷新点。

### 得分
**正常得分**

一名玩家将球射入敌方球门时，记一次正常得分。屏幕会显示“XXX scored for red/blue team（XXX玩家为红/蓝队伍得分）”。

**乌龙球**

一名玩家将球射入己方球门时，记一次乌龙球。屏幕会显示“XXX scored for red/blue team（XXX玩家为红/蓝队伍得分）”。

**助攻得分**

若进球者的球在短时间内来自于其他玩家的传球，则记一次助攻得分。屏幕会显示“XXX scored for red/blue team with a pass from YYY（XXX玩家因YYY的助攻而为红/蓝队伍得分）”。


### 模式
不同模式下的球类玩法大不相同。

- **足球 (football)**  
  将球射入对方球门即可得分。

- **篮球 (basketball)**  
  将球投进两队上方的篮框中即可得分。篮球模式共有五张地图，分别为1.0、2.0、3.0、4.0以及1.0的缩小版，其中1.0为最经典的地图。
    - **特殊机制**: 启用了独特的扣篮系统。

- **轰炸 (bombing)**  
  玩法类似于篮球，但地图地形更为复杂，且球门变为两堵竖直墙体。

- **禁锢球 (soulball)**  
  在该模式中，每名玩家都站在由即死区域围成的一小块范围内。球出现在场地上方，玩家可以释放钩索来争取发球权。将球射进球门即可得分。

- **网球 (tennis)**  
  网球模式的地图中通常会出现绿色高台和用来分隔两队的即死区域。将球打到高台之外的地面上即可得分。
    - **Bug**：嵌入即死区域的球刷新点不会杀掉玩家，这会导致玩家有时可以通过球刷新点来穿过即死区域。

- **排球 (volleyball)**  
  排球模式的地图中通常存在网，网的两侧为地面和水面。将球打到对方地面即可得分，射进水面不得分。该模式共有春、夏、秋、冬四张季节主题的地图。
    - **特殊机制**: 完全禁用钩子功能。
    - *注*：排球模式中的网与网球模式中有相同的bug。

- **太空球 (spaceball)**  
  在太空球模式下，玩家受到的重力会降低，同时球和球门都隐藏在即死区域当中。将球射进球门即可得分。
    - **特殊机制**: 设置了重生延迟。

- **星星球 (starsball)**  
  类似于太空球，同样具有低重力和重生延迟。

- **乒乓球 (tabletennis)**  
  乒乓球模式下有即死区域组成的高台与屏障。将球扔到高台外的地面即可得分。
    - *注*：乒乓球模式和网球模式有同样的bug。

- **破壁球 (wallsmash)**  
  玩法类似于网球，不同点在于多了一块踏板。将球射进球门即可得分。

## 服务器配置变量  

- `sv_ball_respawn`: 用于控制球的刷新间隔时间。
- `sv_keeptime`: 用于控制玩家的最大持球时间。
- `sv_basket`: 用于启用或禁用篮球的扣篮系统。
- `player_hooking`: 用于控制钩子功能的全局开关。

## 参数对比
![各模式参数对比表](resources/foot/info.jpg){.bordered-img tooltip="各模式参数对比表"}

## 官方分支贡献者
<details>
<summary>点我展开</summary>
<a href="https://github.com/TeeworldsCN/teeworlds-teefoot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TeeworldsCN/teeworlds-teefoot&max=999&column=20" alt="贡献者" />
</a>
</details>