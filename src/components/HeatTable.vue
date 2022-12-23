<template>
  <n-space justify="space-between">
    <n-text>
      最受欢迎
    </n-text>
    <n-button
        :type="compareRef.type"
        :disabled="compareRef.flag"
        @click="handleCompare">
      {{ compareRef.text }}
    </n-button>
  </n-space>
  <n-data-table
      :columns="columns"
      :data="data"
      :pagination="pagination"
      @update:sorter="handleSorterChange"
  />
</template>

<script>
import {defineComponent, h, reactive, ref} from "vue";
import {NButton, NImage} from "naive-ui";
import {Add as AddIcon, Remove as RemoveIcon} from "@vicons/ionicons5";
import {useRouter} from "vue-router";
import request from "@/utils/request";


/*
* cur:当前热度（在线人数）
* max:最大热度
* */
// let data = [
//   {
//     game_id: 3,
//     img: "https://cdn.cloudflare.steamstatic.com/steam/apps/1599340/header.jpg?t=1670026493",
//     name: "Houkai 3rd",
//     cur: 99,
//     max: 999
//   },
//   {
//     game_id: 9,
//     img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg",
//     name: "Genshin Impact",
//     cur: 2999,
//     max: 19990
//   },
//   {game_id: 8, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 2, max: 160},
//   {game_id: 2, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 21, max: 150},
//   {game_id: 4, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 22, max: 110},
//   {game_id: 6, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 32, max: 130},
//   {game_id: 8, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 2, max: 160},
//   {game_id: 2, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 21, max: 150},
//   {game_id: 4, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 22, max: 110},
//   {game_id: 6, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 32, max: 130}
// ];

export default defineComponent({
  name: 'HeatTable',
  props: ['searchMsg'],//如果搜索，搜索的内容
  setup(props, {emit}) {
    //对比
    const compareRef = ref({
      flag: ref(true),
      text: ref("选择至少两个进行比较"),
      type: ref("default"),
    })

    const createColumns = ({clickGameName: clickGameName, compareRef: compareRef}) => {
      return [
        {
          title: "排名",
          key: "no",
          width: 120,
          render: (_, index) => {
            return index + 1;
          }
        },
        {
          title: "",//游戏图标
          key: "game_cover",//图片
          width: 140,
          render: (value) => {
            return h(
                NImage,
                {
                  width: 140,
                  height: 40,
                  src: value.game_cover
                }
            )
          }
        },
        {
          title: "游戏名",
          key: "game_name",
          // sortOrder: false,
          // sorter: 'default',
          render: (value) => {
            return h(
                NButton,
                {
                  text: true,
                  type: 'primary',
                  onClick: () => clickGameName(value)
                },
                {default: () => value.game_name}
            )
          }
        },
        {
          title: "当前热度",
          key: "players",
          width: 160,
          sortOrder: false,
          sorter(rowA, rowB) {
            return rowA.cur - rowB.cur
          }
        },
        {
          title: "最高热度",
          key: "max_heat",
          width: 160,
          sortOrder: false,
          sorter(rowA, rowB) {
            return rowA.max - rowB.max
          }
        },
        // 对比按钮
        {
          title: "",
          key: "",
          width: 60,
          render: (rowValue) => {
            const flag = ref(selects.indexOf(rowValue.id)!==-1);
            return h(
                NButton,
                {
                  // 添加/删除按钮
                  onClick: () => {
                    if (flag.value) {
                      // 取消选择
                      selects.pop();
                      if (selects.length < 2) {
                        compareRef.value.flag = true;
                      }
                    } else {
                      // 选择
                      if (!flag.value) {
                        selects.push(rowValue.game_id);
                      }
                      if (selects.length > 1) {
                        compareRef.value.flag = false;
                      }
                    }
                    flag.value = !flag.value;
                  },
                  renderIcon: () => {
                    if (!flag.value) {
                      return h(AddIcon);
                    } else {
                      return h(RemoveIcon);
                    }
                  },
                },
            )
          }
        },
      ];
    };

    // 选择的游戏id
    const selects = [];

    const router = useRouter();

    const data = ref([]);
    //TODO 后端获取数据
    request.post("/getHeat/",JSON.stringify({})).then(res=>{
      // console.log(res.data);
      data.value = res.data;
    });

    const columnsRef = ref(
        createColumns({
          clickGameName(value) {
            //跳转到游戏详情页
            router.push("/detail/"+value.game_id.toString()+"/price");
          },
          compareRef
        })
    )

    // 分页
    const paginationReactive = reactive({
      page: 1,
      showSizePicker: true,
      pageSizes: [
        {
          label: "25/每页",
          value: 25
        },
        {
          label: "50/每页",
          value: 50
        },
        {
          label: "100/每页",
          value: 100
        }
      ],//可选的分页
      pageSize: 25,//初值
      onChange: (page) => {
        paginationReactive.page = page;
      },
      onUpdatePageSize: (pageSize) => {
        paginationReactive.pageSize = pageSize;
        paginationReactive.page = 1;
      }
    })

    return {
      data,
      columns: columnsRef,
      pagination: paginationReactive,
      compareRef,
      handleSorterChange(sorter) {
        columnsRef.value.forEach((column) => {
          /** column.sortOrder !== undefined means it is uncontrolled */
          if (column.sortOrder === undefined) return
          if (!sorter) {
            column.sortOrder = false
            return
          }
          if (column.key === sorter.columnKey) column.sortOrder = sorter.order
          else column.sortOrder = false
        })
      },
      // 点击对比按钮，把选择的游戏id发送给父组件
      handleCompare() {
        emit("changeChart", selects);
      },
    }
  }
});
</script>

<style scoped>

</style>