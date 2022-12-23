<template>
  <div class="reply-comment">
    <!-- 输入框 -->
    <div v-clickoutside="hideReplyBtn" @click="inputFocus" class="my-reply">
      <el-avatar class="header-img" :size="40" :src="myHeader"></el-avatar>
      <div class="reply-info">
        <div tabindex="0" contenteditable="true" id="replyInput" spellcheck="false" placeholder="输入评论..."
             class="reply-input" @focus="openBtn" @input="onDivInput($event)">
        </div>
      </div>
      <div class="reply-btn-box" v-show="btnShow">
        <el-button class="reply-btn" size="" @click="sendComment" type="primary">发表评论</el-button>
      </div>
    </div>

    <!-- /* item 为root评论，i为索引 */ -->
    <div v-for="(item, i) in comments" :key="i" class="author-title reply-father">
      <el-card v-if="i>=pageSize*(curPageIndex-1)&&i<pageSize*curPageIndex" shadow="hover" class="comment-card">
        <!-- 头像 -->
        <el-avatar class="header-img" :size="40" :src="item.avatar"></el-avatar>
        <!-- 根用户信息 -->
        <div class="author-info">
          <span class="author-name">{{ item.name }}</span>
          <span class="author-time">{{ item.time }}</span>
        </div>
        <!-- 根用户的右标签 -->
        <div class="icon-btn">
          <!-- 点赞按钮-->
          <span @click="thumbUp(i, item.flag, item.id)"><i
              class="iconfont el-ic on-s-comment"><el-icon>
            <StarFilled v-if="item.flag===1||item.flag"/>
            <Star v-else/>
                            </el-icon></i>{{
              item.likes
            }}</span>
          <!-- 更多的icon -->
          <i class="iconfont icon-margin">
            <el-dropdown>
                            <span class="el-dropdown-link">
                                <!--more图标-->
                                <el-icon>
                                    <More/>
                                </el-icon>
                            </span>
              <template #dropdown>
                <el-dropdown-menu>
                  <!--                  <el-dropdown-item @click="reportOtherComment"-->
                  <!--                                    v-if="store.state.loggedIn&&store.state.user.userID !== item.id">举报-->
                  <!--                  </el-dropdown-item>-->
                  <el-dropdown-item @click="deleteYourComment(i, item.user_id)"
                                    v-if="store.state.loggedIn&&store.state.user.userID === item.id">删除
                  </el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </i>
        </div>
        <div class="talk-box">
          <!-- 根用户的评论内容 -->
          <p>
            <span class="reply">{{ item.content }}</span>
          </p>
        </div>
        <!-- 子评论 -->
        <!--        <div class="reply-box">-->
        <!--          <div v-for="(reply, j) in item.reply" :key="j" class="author-title">-->
        <!--            &lt;!&ndash; 头像 &ndash;&gt;-->
        <!--            <el-avatar class="header-img" :size="40" :src="reply.fromHeadImg"></el-avatar>-->
        <!--            &lt;!&ndash; 用户信息 &ndash;&gt;-->
        <!--            <div class="author-info">-->
        <!--              <span class="author-name">{{ reply.from }}</span>-->
        <!--              <span class="author-time">{{ reply.time }}</span>-->
        <!--            </div>-->
        <!--            &lt;!&ndash; 图标 &ndash;&gt;-->
        <!--            <div class="icon-btn">-->
        <!--                            <span @click="showReplyInput(i, reply.from, reply.id)"><i-->
        <!--                                class="iconfont el-icon-s-comment"></i><el-icon>-->
        <!--                                    <ChatDotSquare/>-->
        <!--                                </el-icon></span>-->
        <!--              &lt;!&ndash; 更多的icon &ndash;&gt;-->
        <!--              &lt;!&ndash; 更多的icon &ndash;&gt;-->
        <!--              <i class="iconfont icon-margin">-->
        <!--                <el-dropdown>-->
        <!--                                    <span class="el-dropdown-link">-->
        <!--                                        &lt;!&ndash;more图标&ndash;&gt;-->
        <!--                                        <el-icon>-->
        <!--                                            <More/>-->
        <!--                                        </el-icon>-->
        <!--                                    </span>-->
        <!--                  <template #dropdown>-->
        <!--                    <el-dropdown-menu>-->
        <!--                      &lt;!&ndash; 查询vuex比对本评论的fromId如果相同显示删除,否则显示举报 &ndash;&gt;-->
        <!--                      <el-dropdown-item @click="reportOtherComment(reply.commentId)"-->
        <!--                                        v-if="store.state.uid !== reply.fromId">举报-->
        <!--                      </el-dropdown-item>-->
        <!--                      <el-dropdown-item @click="deleteYourComment(i,reply.commentId)" v-else>删除</el-dropdown-item>-->
        <!--                    </el-dropdown-menu>-->
        <!--                  </template>-->
        <!--                </el-dropdown>-->
        <!--              </i>-->
        <!--            </div>-->
        <!--            &lt;!&ndash; 回复评论 &ndash;&gt;-->
        <!--            <div class="talk-box">-->
        <!--              <p>-->
        <!--                <span><el-link class="reply-to-who-link" :underline="false" type="primary">@{{ reply.to }} : </el-link></span>-->
        <!--                <span class="reply">{{ reply.comment }}</span>-->
        <!--              </p>-->
        <!--            </div>-->
        <!--            <div class="reply-box">-->
        <!--            </div>-->
        <!--          </div>-->
        <!--        </div>-->
        <!--        &lt;!&ndash; /* 控制子评论的显示 */ &ndash;&gt;-->
        <!--        <div v-show="_inputShow(i)" class="my-reply my-comment-reply">-->
        <!--          <el-avatar class="header-img" :size="40" :src="myHeader"></el-avatar>-->
        <!--          <div class="reply-info">-->
        <!--            <div tabindex="0" contenteditable="true" spellcheck="false" :placeholder="commentReplyToName"-->
        <!--                 @input="onDivInput($event)" class="reply-input reply-comment-input"></div>-->
        <!--          </div>-->
        <!--          <div class=" reply-btn-box">-->
        <!--            <el-button class="reply-btn" size="" @click="sendCommentReply(i)"-->
        <!--                       type="primary">回复评论-->
        <!--            </el-button>-->
        <!--          </div>-->
        <!--        </div>-->
      </el-card>
    </div>


    <!-- 分页插件 -->
    <div class="divide-page">
      <el-pagination background :page-size="pageSize" @current-change="handleCurrentChange" layout="prev, pager, next"
                     :total="commentTotal"/>
    </div>
  </div>
</template>

<script setup>
import {ref, reactive, computed, onMounted} from "vue"
import {ElMessage} from 'element-plus'
import store from "@/store";
import request from "@/utils/request";
import {useRouter} from "vue-router";
import {useMessage} from "naive-ui";


const router = useRouter();
const gameId = parseInt(router.currentRoute.value.params.gameid);

// 临时数据不用获取
// const visitorAvatar = "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"//用户（评论）头像
const btnShow = ref(false);// 展示按钮
const replyComment = ref('');//评论内容
// const to = ref("");
// const toId = ref(-1);
// const index = ref('0');//上一条评论的index?

// 这一部分 ID使用的是Vuex中的数据
// const myName = computed(() => {
//   return store.state.user.nickname;
// })
const myHeader = computed(() => {
  //TODO 未登录时状态是否正确?
  return store.state.user.avatar;
})
// const myId = computed(() => {
//   return store.state.user.userID
// })


const pageSize = ref(10);//每一页的数目(只计算根评论的)
const curPageIndex = ref(1);//当前页号
// const commentTotal = ref(2)// 根评论的总数(数据库中的数目用来调整分页大小)
const commentTotal = ref(computed(() => {
  return comments.value.length
}))

const comments = ref([
  {
    id: 1234554,//评论id
    name: 'linkk',//用户名
    user_id: 19891221,//用户id
    avatar: 'www.baidu.com.png',//用户头像
    content: '安徽省空间按时艰苦实践案例',
    time: '2022年12月16日 18:43',
    flag: false,//是否被该用户点赞
    likes: 1,//点赞人数
  },
  // {
  //   commentId: "1234554",
  //   name: 'linkk',
  //   id: 19891221,
  //   headImg: visitorAvatar,
  //   comment: '安徽省空间按时艰苦实践案例',
  //   time: '2022年12月16日 18:43',
  //   commentNum: 1,
  //   inputShow: false,
  // },
])

//TODO 举报功能
const reportOtherComment = (commentId) => {
  console.log("评论中more图标  函数名:reportOtherComment 作用:举报 评论Id:" + commentId)
}

onMounted(() => {
  let userId = null;
  if (store.state.loggedIn) {
    userId = store.state.user.userID;
  }
  request.post('/getComment/', JSON.stringify({'game_id': gameId, 'user_id': userId})).then((res) => {
    //TODO 得到所有评论
    // console.log(res.data);
    // console.log(comments);
    comments.value=res.data;
  })
})

// 分页
const handleCurrentChange = (val) => {
  // console.log(`current page: ${val}` + "请求数据:")
  // 更新根评论总数以及comment数目
  // console.log(comments);
  // console.log(commentTotal);
  // console.log(val);
  curPageIndex.value = val
}


const openBtn = () => {
  // comments[index.value].inputShow = false;
  btnShow.value = true;
}

//TODO 删除自己的评论
const deleteYourComment = (i, commentId) => {
  console.log("评论中more图标  函数名:deleteYourComment 作用:删除 评论Id:" + commentId)
  request.post('/delComment/', JSON.stringify({'id': commentId})).then(res => {
    comments.value.splice(i, 1);
  })
  // let deleteList = [];//待删除的评论列表
  // if (comments[i].commentId === commentId) {
  //   console.log("根评论(子评论全删除)")
  //   var k = 0;
  //   while (k < comments[i].reply.length) {
  //     deleteList.push(comments[i].reply[k].commentId)
  //     k++;
  //   }
  //   comments.splice(i, 1);//移除该评论组
  // } else {
  //   var k = 0;
  //   while (k < comments[i].reply.length) {
  //     if (comments[i].reply[k].commentId === commentId) {
  //       comments[i].reply.splice(k, 1);//移除该评论
  //       break;
  //     }
  //     k++;
  //   }
  //   console.log("子评论,只删除该评论")
  // }
  // deleteList.push(commentId);
  // console.log("调用函数deleteList 删除的列表commentId=>" + deleteList);
  // deleteCommentList(deleteList);
}
// const deleteCommentList = (deleteList) => {
//   console.log("函数名:deleteList 待删除列表:" + deleteList)
// }
// const commentReplyToName = computed(() => {
//   return "@" + to.value;
// });


// function
const hideReplyBtn = () => {
  btnShow.value = false
  replyInput.style.padding = "10px"
  replyInput.style.border = "none"
}
const inputFocus = () => {
  var replyInput = document.getElementById('replyInput');
  replyInput.style.padding = "8px 8px";
  replyInput.style.border = "2px solid bule";
  replyInput.focus();

}
// const showReplyBtn = () => {
//   btnShow.value = true
// }
const onDivInput = (e) => {
  replyComment.value = e.target.innerHTML;
}
/* 自定义指令 v-clickoutside */
const vClickoutside = {
  // 初始化指令
  beforeMounted(el, binding, vnode) {
    function documentHandler(e) {
      // 这里判断点击的元素是否是本身，是本身，则返回
      if (el.contains(e.target)) {
        return false;
      }
      // 判断指令中是否绑定了函数
      if (binding.expression) {
        // 如果绑定了函数 则调用那个函数，此处binding.value就是handleClose方法
        binding.value(e);
      }
    }

    // 给当前元素绑定个私有变量，方便在unbind中可以解除事件监听
    el.vueClickOutside = documentHandler;
    document.addEventListener('click', documentHandler);
  },
  unmounted(el, binding) {
    // 解除事件监听
    document.removeEventListener('click', el.vueClickOutside);
    delete el.vueClickOutside;
  },
};
// 顶部'发表评论'按钮函数

//TODO 发布评论
const sendComment = () => {
  if (!store.state.loggedIn) {
    ElMessage({
      showClose: true,
      type: 'error',
      message: '请先登录'
    })
    return;
  }
  if (!replyComment.value) {
    ElMessage({
      showClose: true,
      type: 'warning',
      message: '评论不能为空'
    })
  } else {
    let post = {
      game_id: gameId,
      user_id: store.state.user.userID,
      content: replyComment.value,
    }
    request.post('/addComment/', JSON.stringify(post)).then(res => {
      console.log(res.data);
      comments.value.unshift(res.data);
      replyComment.value = '';
      // document.getElementById('replyInput').innerHTML = '';
    })
  }

  // console.log(myId.value);
  // if (!replyComment.value) {
  //   ElMessage({
  //     showClose: true,
  //     type: 'warning',
  //     message: '评论不能为空'
  //   })
  // } else {
  //   let a = {}
  //   let input = document.getElementById('replyInput')
  //   let timeNow = new Date().getTime();
  //   let time = dateStr(timeNow);
  //   console.log("需要获取一个评论的id,这里默认设置的12251")
  //   a.commentId = "12251"
  //   a.name = myName.value
  //   a.comment = replyComment.value
  //   a.headImg = myHeader.value
  //   a.time = time
  //   a.commentNum = 0
  //   a.reply = []
  //   a.id = store.state.uid;
  //   a.inputShow = false;
  //   comments.push(a)
  //   replyComment.value = ''
  //   input.innerHTML = '';
  // }
}

//TODO showReplyInput改为绑定点赞/取消赞的函数
const thumbUp = (i, flag, comment_id) => {
  console.log(comments.value[i].flag);
  console.log(i);
  if (!store.state.loggedIn) {
    ElMessage({
      showClose: true,
      type: 'error',
      message: '请先登录'
    })
    return;
  }
  let post = {
    'user_id': store.state.user.userID,
    'comment_id': comment_id,
    'type': 'like',
  }
  if (flag === 1) {
    post.type = 'dislike';
  }
  request.post('/updateComment/', JSON.stringify(post)).then(res => {
    comments.value[i].flag = 1-flag;
    if(comments.value[i].flag===1){
      comments.value[i].likes++;
    }else {
      comments.value[i].likes--;
    }
  })
}
// 根评论的回复框
// const showReplyInput = (i, name, id) => {
//   // console.log(store.state.uid)
//   /* 原先的回复框取消 */
//   comments[index.value].inputShow = false;
//   index.value = i;
//   comments[i].inputShow = true;
//   to.value = name;//@+回复的人的姓名
//   toId.value = id;//@+回复的人的id
//   btnShow.value = false;
// }
// 在第i个根评论显示回复框
// const _inputShow = (i) => {
//   return comments[i].inputShow;
// }
/* 根评论下的子评论 */
// const sendCommentReply = (i) => {
//   if (!replyComment.value) {
//     ElMessage({
//       showClose: true,
//       type: 'warning',
//       message: "评论不能为空"
//     })
//   } else {
//     console.log("函数:sendCommentReply 作用:插入评论 参数:评论 ==== 需要一个评论id")
//     let a = {}
//     let timeNow = new Date().getTime();
//     let time = dateStr(timeNow);
//
//
//     a.commentId = "2521255"
//     a.from = myName.value
//     a.to = to.value
//     a.fromHeadImg = myHeader.value
//     a.comment = replyComment.value
//     a.time = time
//     a.commentNum = 0
//     comments[i].reply.push(a)
//     comments[i].commentNum++;
//     replyComment.value = ''
//     document.getElementsByClassName("reply-comment-input")[i].innerHTML = ""
//   }
// }

//TODO 时间戳
// const dateStr = (date) => {
//   //获取js 时间戳
//   var time = new Date().getTime();
//   //去掉 js 时间戳后三位，与php 时间戳保持一致
//   time = parseInt((time - date) / 1000);
//   //存储转换值
//   var s;
//   if (time < 60 * 10) {//十分钟内
//     return '刚刚';
//   } else if ((time < 60 * 60) && (time >= 60 * 10)) {
//     //超过十分钟少于1小时
//     s = Math.floor(time / 60);
//     return s + "分钟前";
//   } else if ((time < 60 * 60 * 24) && (time >= 60 * 60)) {
//     //超过1小时少于24小时
//     s = Math.floor(time / 60 / 60);
//     return s + "小时前";
//   } else if ((time < 60 * 60 * 24 * 30) && (time >= 60 * 60 * 24)) {
//     //超过1天少于30天内
//     s = Math.floor(time / 60 / 60 / 24);
//     return s + "天前";
//   } else {
//     //超过30天ddd
//     var date = new Date(parseInt(date));
//     return date.getFullYear() + "/" + (date.getMonth() + 1) + "/" + date.getDate();
//   }
// }
</script>

<style lang="stylus" scoped>
.reply-to-who-link
  font-size 17px
  text-align center
  margin-right 5px

.comment-card
  border-radius 20px

.divide-page
  display flex
  justify-content center


.reply-comment
  text-align left
  width 668px
  font-family Microsoft YaHei

.my-reply
  padding 10px
  background-color #fafbfc

  .header-img
    display inline-block
    vertical-align top

  .reply-info
    display inline-block
    margin-left 5px
    width 80%
    @media screen and (max-width: 1200px) {
      width 80%
    }

    .reply-input
      min-height 20px
      line-height 22px
      padding 10px 10px
      color #ccc
      background-color #fff
      border-radius 5px

      &:empty:before
        content attr(placeholder)

      &:focus:before
        content none

      &:focus
        padding 8px 8px
        border 2px solid blue
        box-shadow none
        outline none

  .reply-btn-box
    height 25px
    margin 10px 0

    .reply-btn
      position relative
      float right
      margin-right 15px

.my-comment-reply
  margin-left 50px

  .reply-input
    width flex

.author-title:not(:last-child)
.author-title
  padding 10px

  .header-img
    display inline-block
    vertical-align top

  .author-info
    display inline-block
    margin-left 5px
    width 60%
    height 40px
    line-height 20px

    > span
      display block
      cursor pointer
      overflow hidden
      white-space nowrap
      text-overflow ellipsis

    .author-name
      color #000
      font-size 18px
      font-weight bold

    .author-time
      font-size 14px

  .icon-btn
    width 25%
    padding 0 !important
    float right
    @media screen and (max-width: 1200px) {
      width 20%
      padding 7px
    }

    > span
      cursor pointer

    .iconfont
      margin 0 5px

    .icon-margin
      margin-left 25px

  .talk-box
    margin 0 50px

    > p
      margin 0

    .reply
      font-size 16px
      color #000

  .reply-box
    margin 10px 0 0 50px
    background-color #efefef
</style>