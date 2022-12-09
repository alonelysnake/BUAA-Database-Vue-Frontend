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
      key: "icon",//图片
      width: 140,
      render: (value) => {
        return h(
            NImage,
            {
              width: 140,
              height: 40,
              src: value.img
            }
        )
      }
    },
    {
      title: "游戏名",
      key: "name",
      sortOrder: false,
      sorter: 'default',
      render: (value) => {
        return h(
            NButton,
            {
              text: true,
              type: 'primary',
              onClick: () => clickGameName(value)
            },
            {default: () => value.name}
        )
      }
    },
    {
      title: "当前热度",
      key: "cur",
      width: 160,
      sortOrder: false,
      sorter(rowA, rowB) {
        return rowA.cur - rowB.cur
      }
    },
    {
      title: "最高热度",
      key: "max",
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
      render: () => {
        const flag = ref(false);
        return h(
            NButton,
            {
              //TODO 添加/删除
              onClick: () => {
                if (flag.value) {
                  //TODO 取消选择
                  selects.pop();
                  if (selects.length < 2) {
                    compareRef.value.flag = true;
                  }
                } else {
                  //TODO 选择
                  selects.push(1);
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

//TODO 改成字典? 选择进行比较的游戏
const selects = [];

/*
* cur:当前热度（在线人数）
* max:最大热度
* */
const data = [
  {
    id: 3,
    img: "https://cdn.cloudflare.steamstatic.com/steam/apps/1599340/header.jpg?t=1670026493",
    name: "Houkai 3rd",
    cur: 99,
    max: 999
  },
  {
    id: 9,
    img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg",
    name: "Genshin Impact",
    cur: 2999,
    max: 19990
  },
  {id: 8, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 2, max: 160},
  {id: 2, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 21, max: 150},
  {id: 4, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 22, max: 110},
  {id: 6, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 32, max: 130},
  {id: 8, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 2, max: 160},
  {id: 2, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 21, max: 150},
  {id: 4, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 22, max: 110},
  {id: 6, img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 32, max: 130}
];

export default defineComponent({
  name: 'HeatTable',
  setup() {
    //对比
    const compareRef = ref({
      flag: ref(true),
      text: ref("选择至少两个进行比较"),
      type: ref("default"),
    })

    console.log(compareRef.value);

    const columnsRef = ref(
        createColumns({
          clickGameName(value) {
            //TODO 跳转到游戏详情页，路由为 'gameinfo/游戏id'的样子？
            console.log(value.id)
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
      //TODO 对比函数（跳转到对比界面）
      handleCompare() {

      },
    }
  }
});
</script>

<style scoped>

</style>