<template>
  <div>
    <div class="navbar">
      <span class="navbar-text">{{title}}</span>
    </div>

    <div class="content">
      <div>
        <ul class="message-content" ref="messageContent"> <!--可以被JS的$refs.messageContent 来捕获-->
          <li v-for="(item, index) in msgRecord" :key="index">
            <chat-item :chatItemObj="item"></chat-item> <!--这个是chat-item组件的props里面的属性，用来同步更新父组件的数据-->
          </li>
        </ul>
      </div>

      <chat-input :inputDisable="inputDisable" :meDatas="meDatas" @onMeSelectMsg="onMeSelectMsg"></chat-input>
    </div>

  </div>

</template>

<script>
import ChatItem from '../components/ChatItem.vue'
import ChatInput from '../components/ChatInput.vue'
export default {
  components: { // 我们引用了其他组件。不要以为没有导出自己，这些组件只是表示了子组件而已
    'chat-item': ChatItem, // 模板:组件
    'chat-input': ChatInput
  },
  data: function () {
    return {
      title: 'Chatting...',
      inputDisable: true, // Machine 回答时，禁止我对话
      chatData: [], // 数据源
      selectMsgData: {}, // 选中的聊天数据
      msgRecord: [], // 显示出来的聊天的数据
      meDatas: [] // 我可以选择的话(数据)
    }
  },
  created: function () { // 不是mounted，这时候还没有挂载$el
    this.loadChatData()
  },
  methods: {

    /* 当内容溢出视区时，需要滚动 */
    scrollContent: function () {
      this.$nextTick(function () { // 具有马上更新的功能，注意：与setTimeout 不同，一个是 macrotask,一个是microtask
        var msgContent = this.$refs.messageContent
        msgContent.scrollTop = msgContent.scrollHeight // 我也不知道为什么要这样，但是发现效果不错
      })
    },

    /* 获取数据 */
    loadChatData: function () {
      var $this = this
      this.$http.get('../../static/chatData.json')
        .then(function (res) {
          $this.chatData = res.data.msgData // 把获取的数据存起来, 而且并不是直接的 "msgData"
          $this.setMsg('000') // 选择对话
        })
    },

    /* 选择‘我’要说的话 */
    setMsg: function (selectId) {
      this.selectMsgData = this.chatData.filter((item) => {
        return item.id === selectId
      })[0] // 注意这里的是数组，所以我们需要pick出来一个数据
      this.setMsgRecord(this.selectMsgData.machineMsg, 'machine')
      this.meDatas = this.selectMsgData.meData
    },

    /* 对聊天内容分层‘机器人’和‘我’两类 */
    setMsgRecord: function (msgData, type) {
      var $this = this
      var i = 0
      if ('machine' === type) {
        $this.title = 'machine is writting...'
        $this.inputDisable = true

        /* 一条一条来显示机器人的话 */
        var interval = setInterval(function () {
          $this.msgRecord.push({ // 注意聊天记录是一个数组来存储
            id: $this.selectMsgData.id,
            msg: msgData[i], // machineMsg也是一个数组
            type: type
          })
          $this.scrollContent()
          i++

          if (i >= msgData.length) { // 表示 Machine 如果讲完话了，那么我就可以说话并且清除定时器
            $this.title = 'Chatting...'
            $this.inputDisable = false
            window.clearInterval(interval)
            return;
          }
        }, 1000) // 延迟一秒来显示 Machine 的话，但多条语句时候不会一次性显示出来
      } else {
        this.msgRecord.push({
          id: $this.selectMsgData.id,
          msg: msgData[0], // 因为这也是数组，但是只用一句话
          type: type
        })
        $this.scrollContent()
      }
    },

    /* 点击‘我’的选择区 */
    onMeSelectMsg: function (item) {

      /* 先直接push我的话，然后机器人在说话 */
      this.setMsgRecord(item.meMsg, 'me')
      this.setMsg(item.id)
    }
  }
}
</script>

<style scoped lang="less">

  .navbar {
    height: 44px;
    display: flex;
  }

  .navbar-text {
    margin: 0 auto;
    line-height: 44px;
  }


  .content {
    position: absolute;
    overflow: hidden;
    top: 44px;
    bottom: 0;
    right: 0;
    left: 0;
    background: linear-gradient(to bottom, #57b1ff, #c0e2ff);
  }

  .message-content {
    position: absolute;
    top: 0;
    bottom: 45px;
    width: 100%;
    overflow-x: hidden;
    overflow-y: scroll;
  }

  .animated {
      -webkit-animation-duration: .4s;
      animation-duration: .4s;
  }


</style>
