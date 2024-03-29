<template>
  <n-data-table
      :columns="columns"
      :data="dataRef"
      :pagination="pagination"
      @update:sorter="handleSorterChange"
      :bordered="false"
  />
</template>

<script>
import {h, reactive, ref} from "vue";
import {NButton, NImage} from "naive-ui";
import {useRouter} from "vue-router";
import request from "@/utils/request";

const createColumns = ({clickGameName: clickGameName}) => {
  return [
    {
      title: "",//游戏图标
      key: "cover",//图片
      width: 140,
      render: (value) => {
        return h(
            NImage,
            {
              width: 140,
              height: 40,
              src: value.cover
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
        const dc = Math.floor((100-value.discount_rate) / 5) * 5;
        return '-' + dc + '%';
      }
    },
    {
      title: "优惠价",
      key: "current_price",
      sortOrder: false,
      sorter(rowA, rowB) {
        return rowA.current_price - rowB.current_price
      },
      render: (value) => {
        return '￥' + value.current_price;
      }
    },
    {
      title: "rating",
      key: "discount_rate",
      render: (value) => {
        return value.discount_rate + "%";
      }
    },
    {
      title: "起始时间",
      key: "start_time"
    },
    {
      title: "结束时间",
      key: "end_time"
    }
  ];
};

/*
* */
const datas = [
  // {
  //   id: 3,
  //   cover: "https://cdn.cloudflare.steamstatic.com/steam/apps/1599340/header.jpg?t=1670026493",
  //   name: "Houkai 3rd",
  //   discount_rate: 84.75,
  //   current_price: 12.5,
  //   start_time: "2020-3-5",
  //   end_time: "2023-2-2"
  // },
  // {
  //   id: 3,
  //   img: "https://cdn.cloudflare.steamstatic.com/steam/apps/33230/header.jpg?t=1667609065",
  //   name: "Assassin's Creed 2",
  //   rating: 60,
  //   curPrice: 18.32,
  //   start: "2022-12-1",
  //   end: "2022-12-29"
  // },
  // {
  //   id: 8,
  //   img: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg",
  //   name: "aa",
  //   rating: 60,
  //   curPrice: 18.32,
  //   start: "2022-12-1",
  //   end: "2022-12-29"
  // },
  // {
  //   id: 1,
  //   cover: "https://img2.baidu.com/it/u=4215021439,1696788421&fm=253&fmt=auto&app=138&f=JPEG?w=649&h=317",
  //   name: "genshin",
  //   discount_rate: 63.00,
  //   current_price: 20.00,
  //   start_time: "2022-12-1",
  //   end_time: "2022-12-17"
  // },
  // {
  //   id: 2,
  //   cover: "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fmedia.9game.cn%2Fgamebase%2Fieu-gdc-pre-process%2Fimages%2F20220711%2F2%2F18%2F3490f9ea2e8f29cf548ee50a936c6ffe.jpg&refer=http%3A%2F%2Fmedia.9game.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1674055256&t=f997ce14cfcbcaa7d0138dc762c70ce7",
  //   name: "dnf",
  //   discount_rate: 60.00,
  //   current_price: 100.00,
  //   start_time: "2022-12-1",
  //   end_time: "2022-12-17"
  // },
];

export default {
  name: "FilterShowTable",
  setup() {
    const router = useRouter();
    const columnsRef = ref(
        createColumns({
          clickGameName(value) {
            // 跳转到游戏详情页，路由为 'gameinfo/游戏id'
            router.push("/detail/" + value.id.toString() + "/price");
          }
        })
    )

    //数据ref
    const dataRef = ref(datas);

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

    const handleFilter = (conds) => {
      console.log("向后端查找满足cond的数据");
      console.log(conds);
      //向后端传递数据：
      /*
      * 选择国家
      * 选择开发商
      * 优惠类型
      * 折扣比例最低值
      * 发售时间
      * */
      //TODO
      request.post('/filterGame/', JSON.stringify(conds)).then(res => {
        dataRef.value = res.data;
        console.log(dataRef.value);
        conds.loading.value = false;
      });
    }

    return {
      dataRef,
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