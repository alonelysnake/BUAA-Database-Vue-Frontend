<template>
  <n-data-table
      :columns="columns"
      :data="data"
      :pagination="pagination"
      @update:sorter="handleSorterChange"
      :bordered="false"
  />
</template>

<script>
import {h, reactive, ref} from "vue";
import {NButton, NImage} from "naive-ui";
import {useRouter} from "vue-router";

const createColumns = ({clickGameName: clickGameName}) => {
  return [
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
      title: "%",
      key: "rating",
      width: 60,
      sortOrder: false,
      sorter(rowA, rowB) {
        return rowA.rating - rowB.rating
      },
      //TODO 按照不同的减免比例渲染不同的底色
      render: (value) => {
        const dc = Math.floor(value.rating / 5) * 5;
        return '-' + dc + '%';
      }
    },
    {
      title: "优惠价",
      key: "curPrice",
      sortOrder: false,
      sorter(rowA, rowB) {
        return rowA.curPrice - rowB.curPrice
      },
      render: (value) => {
        return '￥' + value.curPrice;
      }
    },
    {
      title: "rating",
      key: "rating",
      render: (value) => {
        return value.rating + "%";
      }
    },
    {
      title: "起始时间",
      key: "start"
    },
    {
      title: "结束时间",
      key: "end"
    }
  ];
};

/*
* */
const data = [
  {
    id: 3,
    img: "https://cdn.cloudflare.steamstatic.com/steam/apps/1599340/header.jpg?t=1670026493",
    name: "Houkai 3rd",
    rating: 84.75,
    curPrice: 12.5,//TODO 全部按照人民币显示
    start: "2020-3-5",
    end: "2023-2-2"
  },
  {
    id: 3,
    img: "https://cdn.cloudflare.steamstatic.com/steam/apps/33230/header.jpg?t=1667609065",
    name: "Assassin's Creed 2",
    rating: 60,
    curPrice: 18.32,
    start: "2022-12-1",
    end: "2022-12-29"
  },
  {
    id: 8,
    img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg",
    name: "aa",
    rating: 60,
    curPrice: 18.32,
    start: "2022-12-1",
    end: "2022-12-29"
  },
];

export default {
  name: "FilterShowTable",
  setup() {
    const router = useRouter();
    const columnsRef = ref(
        createColumns({
          clickGameName(value) {
            //TODO 跳转到游戏详情页，路由为 'gameinfo/游戏id'的样子？
            console.log(value.id)
            router.push("/detail/" + value.id.toString() + "/price");
          }
        })
    )

    //分页
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

    //TODO 改变data
    const handleFilter = (conds) => {
      console.log("向后端查找满足cond的数据");
      console.log(conds);
    }

    return {
      data,
      columns: columnsRef,
      pagination: paginationReactive,

      handleFilter,

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
      }
    }
  }
}
</script>

<style scoped>

</style>