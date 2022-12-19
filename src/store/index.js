import { createStore } from 'vuex'

export default createStore({
    // state,提供唯一的公共数据源，所有共享数据统一放到store的state中进行存储
    // 访问方式: this.$store.state.数据名
    state: {
        loggedIn: true,
        searchItem: "",
        user: {
            nickname: "Veronica",
            userID: '1',
            sales: 40207,
            // 头像Url
            avatar: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg",
            email: "837826068@qq.com",
            intro: "爱打电动的BUAAer",
            sex: "secret",
            like:207,
            dislike:10207,
        },
        good: {
          goodId: -1,
          name: "nier",
          CDKey: "123",
          money: 20.5,
          steamId: "kazeya9",
          intro: "CDKey",
        },
        addGoodsVisible: false,
        editGoodsVisible: false,
        appraiseVisible: false,
        modifyVisible: false,
        rateGoodsId: -1,
    },

    // mutation用于修改store中的数据
    mutations: {
        // 触发mutation的方法：this.$store.commit('方法名')
        login(state,data) {
            state.loggedIn = true;
            state.user.username = data.username;
            state.user.userID = data.userID;
            state.user.avatar = data.avatar;
        },
        logout(state) {
            state.loggedIn = false;
            state.user.username = '';
        },
        setAvatarUrl(state, data) {
            state.user.avatar = data.avatar;
        },
        setInfo(state, data) {
            state.user.nickname = data.nickname;
        },
        test(state) {
            state.count++;
        }
    },
    // 处理异步任务，在action中调用mutation的函数(commit)
    // 使用this.$store.dispatch('方法名')调用
    actions: {
    },
    modules: {
    }
})
