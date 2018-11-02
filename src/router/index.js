import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
  }
**/
export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  { path: '/404', component: () => import('@/views/404'), hidden: true },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    name: 'Dashboard',
    hidden: false,
    children: [{
      path: 'dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '主页', icon: 'table' }
    }]
  },

  {
    path: '/dealer',
    component: Layout,
    // redirect: '/dealer/index',
    // name: 'Example',
    alwaysShow: true,
    meta: { title: '经销商管理', icon: 'example' },
    children: [
      {
        path: '/dealer/index',
        name: 'dealer',
        component: () => import('@/views/dealer/index'),
        meta: { title: '经销商管理', icon: 'table' }
      },
    ]
  },




  { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})




export const asyncRouterMap = [

  {
    path: '/investor',
    component: Layout,
    alwaysShow: true,
    meta: { title: '资方管理', icon: 'example' },
    children: [
      {
        path: '/investor/index',
        name: 'investor',
        component: () => import('@/views/investor/index'),
        meta: { title: '资方管理', icon: 'table' }
      },
    ]
  },

  {
    path: '/financing',
    component: Layout,
    alwaysShow: true,
    meta: { title: '融资管理', icon: 'example' },
    children: [
      {
        path: '/financing/order/index',
        name: 'order',
        component: () => import('@/views/financing/order/index'),
        meta: { title: '订单管理', icon: 'table' }
      },
      {
        path: '/financing/appeal/index',
        name: 'appeal',
        component: () => import('@/views/financing/appeal/index'),
        meta: { title: '申诉管理', icon: 'table' }
      },
    ]
  },

  {
    path: '/permissions',
    component: Layout,
    alwaysShow: true,
    meta: { title: '权限管理', icon: 'example' },
    children: [
      {
        path: '/permissions/role/index',
        name: 'role',
        component: () => import('@/views/permissions/role/index'),
        meta: { title: '角色管理', icon: 'table' }
      },
      {
        path: '/permissions/user/index',
        name: 'user',
        component: () => import('@/views/permissions/user/index'),
        meta: { title: '用户管理', icon: 'table' }
      },
    ]
  },

  {
    path: '/administrativeApproval',
    component: Layout,
    alwaysShow: true,
    meta: { title: '审批管理', icon: 'example' },
    children: [
      {
        path: '/administrativeApproval/mySheet/index',
        name: 'mySheet',
        component: () => import('@/views/administrativeApproval/mySheet/index'),
        meta: { title: '我的审批单', icon: 'table' }
      },
      {
        path: '/administrativeApproval/processDesign/index',
        name: 'processDesign',
        component: () => import('@/views/administrativeApproval/processDesign/index'),
        meta: { title: '流程设计', icon: 'table' }
      },
      {
        path: '/administrativeApproval/processManagement/index',
        name: 'processManagement',
        component: () => import('@/views/administrativeApproval/processManagement/index'),
        meta: { title: '流程管理', icon: 'table' }
      },
    ]
  },

]
