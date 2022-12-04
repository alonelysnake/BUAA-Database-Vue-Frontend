import { createStore } from 'vuex'

export default createStore({
    // state,提供唯一的公共数据源，所有共享数据统一放到store的state中进行存储
    // 访问方式: this.$store.state.数据名
    state: {
        loggedIn: true,
        searchItem: "",
        user: {
            nickname: "Veronica",
            userID: 'VeronicaID',
            type:1,
            // 头像Url
            avatar: "",
        },
        addGoodsVisible: false,
        editGoodsVisible: false,
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
